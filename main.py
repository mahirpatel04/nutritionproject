from datetime import date
from classFood import Food
from classMenu import Menu



def getUserInput():
    """
    User will enter their information

    Returns:
        _list_: Returns list containing information about the user which will be
                later used
    """
    
    print('''Welcome to the Nutrition App!
    This application was created to promote a healthy lifestyle for students at the University of California, Riverside.
    We have tailored this app to align with the residents' dining menu.
    Please enter the required information to get started.''')
    height = float(input("Enter your height in centimeters: " + "cm"))
    weight = float(input("Enter yout weight in kilograms: " + "kg"))
    sex = input("Enter your sex (Male/Female): ")
    age = float(input("Enter your age: " + "years old"))
    meat = input("Are you vegetarian? (Yes/No): ")
    activity_level = input("Enter your activity level: Sedentary, Lightly active, Moderately active, Very active, Extra active: ")
    return [height, weight, sex, age, meat, activity_level]

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







'''''
def CalculateProtein(self, sex, height, age, weight):
    protein = 0.0
    if sex.lower == "male":
        protein = 1.2 * height - 0.2 * age + 0.3 * weight + 10
    elif sex.lower == "female":
        protein = 1.0 * height - 0.1 * age + 0.2 * weight + 5
    
    return protein

def CalculateCalories(self, sex, height, age, weight, activity_level):
    calories = 0.0
    if sex == "male":
        calories = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    elif sex.lower == "female":
        calories = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
    if activity_level.lower == "sedentary":
        calories *= 1.2
    if activity_level.lower == "lightly active":
        calories *= 1.375
    if activity_level.lower == "moderately active":
        calories *= 1.55
    if activity_level.lower == "very active":
        calories *= 1.725
    if activity_level.lower == "Extra active":
        calories *= 1.9
    else:
        print("Activity level is not listed")
     
    return calories
'''       

'''
 # testing 
print("TEST CASES") 
breakfast = [

    Food("Yogurt", 200, 1, "breakfast")

]

lunch = [

    Food("Pork", 400, 1, "lunch")

]

dinner = [
    Food("Rice and chicken", 550, 1, "dinner")
]

print("Breakfast items:")
for item in Menu.breakfast:
    print(f"Name: {item.name}, Calories: {item.calories}, Serving Size: {item.servingSize}")
print("\nLunch items:")
for item in Menu.lunch:
    print(f"Name: {item.name}, Calories: {item.calories}, Serving Size: {item.servingSize}")
print("\nDinner items:")
for item in Menu.dinner:
    print(f"Name: {item.name}, Calories: {item.calories}, Serving Size: {item.servingSize}")

'''