class Food:
    def __init__(self, name, calories, servingSize, mealType):
        self.name = name
        self.calories = int(calories)
        self.mealType = mealType
        self.numServings = 0
    

        if (servingSize[0:2] == "1/2"):
            self.servingSize = 0.5
            self.servingType = servingSize[3::]
        elif (servingSize[0:3] == "1 /2"):
            self.servingSize = 0.5
            self.servingType = servingSize[4::]
        
        else:
            self.servingSize = int(servingSize[0])
            self.servingType = servingSize[1::]