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
            rLst: 
            
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
            caloriePerServing = int(text[2].text[9::])
            servingSize = (text[1].text)
            if (caloriePerServing != 0):     
                rLst.append(Food(items[i].text, caloriePerServing, servingSize, mealType))   
            
        
        self.menuItems = rLst
    def display(self):
        for i in range(len(self.menuItems)):
            print(self.menuItems[i].name + " has " + str(self.menuItems[i].calories) + " calories per " + str(self.menuItems[i].servingSize))

    # put all items that are B L D into their categories
    def categorizeItems(self):
        self.breakfast = []
        self.lunch = []
        self.dinner = []



        for item in self.menuItems:
            if item.mealType == "breakfast":
                self.breakfast.append(item)
            elif item.mealType == "lunch":
                self.lunch.append(item)
            elif item.mealType == "dinner":
                self.dinner.append(item)









"""
# calculate calories for each type of meal. Will need to fix later

def getCaloriesForBreakfast(self):
    total_calories = 0
    for item in self.breakfast:
        total_calories += item.calories * item.servingSize
    return total_calories

def getCaloriesForLunch(self):
    total_calories = 0
    for item in self.lunch:
        total_calories += item.calories * item.servingSize
    return total_calories

def getCaloriesForDinner(self):
    total_calories = 0
    for item in self.dinner:
        total_calories += item.calories * item.servingSize
    return total_calories
"""














"""
# SHOVE IN MAIN: FIND CALORIE INTAKE FIRST THEN ADJUST FOR PROTEIN BASED
def calorieGoal(self, sex, height, age, weight, calorieGoal, proteinGoal):
    selectedItems = []
    for mealType in [self.breakfast, self.lunch, self.dinner]:
        for item in mealType:
            if item.calories * item.servingSize <= calorieGoal:
                selectedItems.append(item)

    proteinRecommendation = self.calculateRecommendedProtein(sex, height, age, weight)
    adjustedItems = []
    for item in selectedItems:
        if item.protein * item.servingSize <= proteinRecommendation:
            adjustedItems.append(item)
    return adjustedItems
"""


"""
    def convertForCalories(self, calorieGoal):
        # Converts menu's original items into items with adjusted serving size quantities to meet the goals
        total_calories = 0
        
        for mealType in [self.breakfast, self.lunch, self.dinner]:
            for item in mealType:
                total_calories += item.calories * item.servingSize

        # do if total_calories exceeds users cals
        if total_calories > calorieGoal:
            simplified_Cals = calorieGoal / total_calories
            
        return self
    """
        
        
        
        