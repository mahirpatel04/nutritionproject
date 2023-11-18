print('''Welcome to the Nutrition App!
This application was created to promote a healthy lifestyle for students at the University of California, Riverside.
We have tailored this app to align with the residents' dining menu.
Please enter the required information to get started.''')
height = float(input("Enter your height in centimeters: "))
weight = float(input("Enter yout weight in kilograms: "))
sex = input("Enter your sex (Male/Female): ")
age = float(input("Enter your age: "))
meat = input("Are you vegetarian? (Yes/No): ")
activity_level = input("Enter your activity level: Sedentary, Lightly active, Moderately active, Very active, Extra active: ")
print(height, weight, sex, age, meat, activity_level)