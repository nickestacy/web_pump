import time
import os

import functions

filenames = ["bodyweight.txt", "protein.txt", "calories.txt",
             "meals.txt", "meals_protein.txt", "meals_calories.txt"]
for filename in filenames:
    if not os.path.exists(filename):
        with open(f"{filename}", 'w') as file:
            pass

username = "laurelhwilliams"
password = "shredded"

bw = 130
goals = [int(bw*1.2), int(bw*16)]

database = functions.readfile(filenames[3])
data_protein = functions.readfile(filenames[4])
data_calories = functions.readfile(filenames[5])

database_dict = {}
for i, meal in enumerate(database):
    protein = data_protein[i]
    calories = data_calories[i]
    database_dict[meal.strip()] = {"protein": protein, "calories": calories}

with open(filenames[3], 'w') as file:
    file.write('\n'.join(list(database_dict.keys())))

timestamp = time.strftime("%d%H%M%b%Y").upper()
title = f"Pump Time {timestamp}"

meal_data = []
totalProtein = 0
totalCalories = 0
