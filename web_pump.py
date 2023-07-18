import streamlit as stream
import functions
import pump


def add_meal():
    meal = stream.session_state["NEW_MEAL"].split("/") +"\n"
    meal_name = meal[0].strip(" ").title()
    meal_protein = int(meal[1].strip(" "))
    meal_calories = int(meal[2].strip(" "))

    pump.database_dict[meal_name] = {"protein": meal_protein, "calories": meal_calories}

    functions.writefile(meal_name, pump.filenames[3], append=True)
    functions.writefile(str(meal_protein), pump.filenames[4], append=True)
    functions.writefile(str(meal_calories), pump.filenames[5], append=True)

    meals = functions.readfile(pump.filenames[3])
    meals_protein = functions.readfile(pump.filenames[4])
    meals_calories = functions.readfile(pump.filenames[5])

    for i, meal in enumerate(meals):
        meal_name = meal.strip()
        meal_protein = meals_protein[i]
        meal_calories = meals_calories[i]
        key = f"{i}_{meal_name}"
        stream.checkbox(f"{meal_name} - Protein: {meal_protein}, Calories: {meal_calories}", key=key)


meals = functions.readfile(pump.filenames[3])
stream.title("Pump It!")
stream.subheader("\"If it jiggles, it's fat\" \n -Arnold Schwarzenegger")
stream.write("This application is to aid in calculating daily macros, for lunks only")

if meals:
    meals_protein = functions.readfile(pump.filenames[4])
    meals_calories = functions.readfile(pump.filenames[5])

    # for index, meal in enumerate(meals):
    #     stream.checkbox(meal, key=meal)
    #     if checkbox:
    #         meals.pop(index)
    #         functions.writefile(meals)
    #         del stream.session_state(meal)  # This deletes it from the ss dictionary
    #         stream.experimental_rerun()  # Rerun the code for the checkboxes
    # for i, meal in enumerate(meals):
    #     meal_name = meal.strip()
    #     meal_protein = meals_protein[i]
    #     meal_calories = meals_calories[i]
    #     key = f"{i}_{meal_name}"
    #     stream.checkbox(f"{meal_name} - Protein: {meal_protein}, Calories: {meal_calories}", key=key)

stream.text_input(label="", placeholder="Add New Meal...", on_change=add_meal, key="NEW_MEAL")
stream.session_state  # This should help you see what is going on
