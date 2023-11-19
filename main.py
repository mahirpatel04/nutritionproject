from datetime import date
from classFood import Food
from classMenu import Menu


def calorieRequirement(userInfo):
    height = userInfo[0]
    weight = userInfo[1]
    sex = userInfo[2]
    age = userInfo[3]
    activity_level = userInfo[4]
                        
    if sex.lower() == "m":
        bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    else:
        bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)


    if (activity_level ==  1):
        calorieEstimate = bmr * 1.2
        
    elif (activity_level == 2):
        calorieEstimate = bmr * 1.375
        
    elif (activity_level == 3):
        calorieEstimate = bmr * 1.55
        
    elif (activity_level == 4):
        calorieEstimate = bmr * 1.725
        
    elif (activity_level == 5):
        calorieEstimate = bmr * 1.9
        
    else:
        print("Activity level is not listed")

    return calorieEstimate
    
def setUrl(inputDay, preferredRestaurant, mealType):
    """
    Sets the url based on the date and which restaurant the user wants to eat at

    Args:
        inputDay (Date): Today's date, used to get the day, month, and year components

    Returns:
        url (str): Returns the url
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

    
 


'''
userInput = getUserInput()
print(userInput)
'''

today = date.today()
url = setUrl(today, "Glasgow", "Lunch")

breakfastItems = Menu(url, "Lunch")

breakfastItems.display()




'''lunchItems = createFoodList(url, "Lunch")
dinnerItems = createFoodList(url, "Dinner")'''






userInfo = getUserInput()

today = date.today()

url_breakfast = setUrl(today, "Glasgow", "Breakfast")
url_lunch = setUrl(today, "Glasgow", "Lunch")
url_dinner = setUrl(today, "Glasgow", "Dinner")
totalCalRequirement = calorieRequirement(userInfo)
calorie_breakfast =  totalCalRequirement * (1/4)
calorie_lunch =  totalCalRequirement * (3/8)
calorie_dinner = totalCalRequirement * (3/8)

breakfastItems = Menu(url_breakfast, "Breakfast")
lunchItems = Menu(url_lunch, "Lunch")
dinnerItems = Menu(url_dinner, "Dinner")


recommendedBreakfast = breakfastItems.recommendFood(calorie_breakfast)
recommendedLunch = lunchItems.recommendFood(calorie_lunch)
recommendedDinner = dinnerItems.recommendFood(calorie_dinner)

breakfastItems.display()
lunchItems.display()
dinnerItems.display()




'''
def CalculateProtein(self, sex, height, age, weight):
    protein = 0.0
    if sex.lower == "male":
        protein = 1.2 * height - 0.2 * age + 0.3 * weight + 10
    elif sex.lower == "female":
        protein = 1.0 * height - 0.1 * age + 0.2 * weight + 5
    
    return protein
'''