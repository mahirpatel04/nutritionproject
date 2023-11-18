from bs4 import BeautifulSoup
import requests
from datetime import date
from classFood import Food

def getUserInput():
    """
    User will enter their information

    Returns:
        _list_: Returns list containing information about the user which will be
                later used
    """
    
    
    height = float(input("Enter your height in centimeters: "))
    weight = float(input("Enter yout weight in pounds: "))
    sex = input("Enter your sex (Male/Female): ")
    age = float(input("Enter your age: "))
    meat = input("Are you vegetarian? (Yes/No): ") 
    return [height, weight, sex, age, meat]


def setUrl(inputDay, preferredRestaurant, mealType):
    """
    Sets the url based on the date and which restaurant the user wants to eat at

    Args:
        inputDay (Date): Today's date, used to get the day, month, and year components

    Returns:
        url (str): returns the url
    """
    
    
    day = str(inputDay.day)
    month = str(inputDay.month)
    year = str(inputDay.year)
    if (preferredRestaurant == "Glasgow"):
        num = 3
    elif (preferredRestaurant == "Lothian"):
        num = 2
    url = "https://foodpro.ucr.edu/foodpro/longmenu.asp?sName=University+of+California%2C+Riverside+Dining+Services&locationNum=0" + str(num) + "&locationName=" + preferredRestaurant + "&naFlag=1&WeeksMenus=This+Week%27s+Menus&dtdate=" + month + "%2F" + day + "%2F" + year + "&mealName=" + mealType
    return url

def createFoodList(inputUrl, mealType):
      site = requests.get(inputUrl)
      siteData = BeautifulSoup(site.text, "html.parser")
      secondurls = siteData.findAll("a", attrs={"class":"href"})
      names = siteData.findAll("div", attrs={"class":'longmenucoldispname'})
      portions = siteData.findAll("div", attrs={"class":'longmenucolportions'})
      
      for url in siteData:
          print(url.text)
     
 


'''
userInput = getUserInput()
print(userInput)'''
today = date.today()
url = setUrl(today, "Glasgow", "Lunch")

breakfastItems = createFoodList(url, "Lunch")

'''lunchItems = createFoodList(url, "Lunch")
dinnerItems = createFoodList(url, "Dinner")'''







