from classFood import Food

class Menu:
    def __init__(self,  itemsOnMenu):
        self.items = itemsOnMenu
        self.breakfast = []
        self.lunch = []
        self.dinner = []
        self.categorizeItems()
        
# put all items that are B L D into their categories
def categorizeItems(self):
    for item in self.items:
        if item.mealType == "breakfast":
            self.breakfast.append(item)
        elif item.mealType == "lunch":
            self.lunch.append(item)
        elif item.mealType == "dinner":
            self.dinner.append(item)

# adjust menu based on user inputs and meet calorie goal
# Methods

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
    
        
        
        
        