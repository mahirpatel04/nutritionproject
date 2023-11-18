from classFood import Food
import requests
from bs4 import BeautifulSoup
class Menu:
    def __init__(self, inputUrl, mealType):
        '''
        Summary
        Fetches food data from URL for a certain meal type
        Extracts infomration such as number of calories, servings based on the item, name of item
        Creates objects of type Food and stores these objects into the list rList based on data grabbed
        Returns the list of Food objects via rList

        Args:
            inputUrl (str): URL from UCR's Dining service
            mealType (str): Name of meal that is fetched from URL classified as B, L, or D
            
        Returns:
            rLst: Stores each Food object of it's own data(calories, name, servings)
            
        '''
        site = requests.get(inputUrl)
        siteData = BeautifulSoup(site.text, "html.parser")
        items = siteData.findAll("div", attrs={"class":'longmenucoldispname'})
        rLst = []
        for i in range(len(items)):
            tUrl = "https://foodpro.ucr.edu/foodpro/" + items[i].find("a")["href"]
            t = requests.get(tUrl)
            site = BeautifulSoup(t.text, "html.parser")
            table = site.find("table")
            text = table.findAll("font", attrs={"size":"5"})
            caloriePerServing = text[2].text[9::]
            servingSize = text[1].text
            if (caloriePerServing != 0):     
                rLst.append(Food(items[i].text, caloriePerServing, servingSize, mealType))   
            
        
        self.menuItems = rLst
        
        
    def display(self):
        for i in range(len(self.menuItems)):
            print(self.menuItems[i].name + " has " + str(self.menuItems[i].calories) + " calories for " + str(self.menuItems[i].servingSize) + " " + self.menuItems[i].servingType)



    def recommendFood(self, calorieGoal):
        recommendedItems = []
        
        for item in self.menuItems:
            if item.calories * item.servingSize <= calorieGoal:
                recommendedItems.append(item)
        
        
        self.menuItems =  recommendedItems