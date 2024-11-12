"""
Author: Jackson Kelley
Lab: Lab 4
Date: 10/28/2024

Description: Example: This program calculates energy utilized from bipedal
humanoid movement given a specific values related to energy expenditure
Input: Weight, distance, MET value

Output: Calories burned, and a string about recovery

Sources: W3Schools.com, Google search Ai, ChatGPT (no copy/paste),
https://realpython.com/if-name-main-python/
----inputs----

weight = 100
distance = 4 mi
(choice 3)
met_value = 7.5
speed_value = 4.5

----calculations----

weight_kg = 45.3

duration_hours = distance * speed
                 4 * 4.5
               = .88

calories_burned = met_value * weight_kg * duration_hours
                  7.5 * 45.3 * .88
                  298.98
                  math.ceil(298.98)

calories_burned = 299
"""
import math

def calculate_calories_burned(weight_lbs, distance_miles, met_value, speed_mph):
    LB_TO_KG = 0.453

    weight_kg = round(weight_lbs * LB_TO_KG, 3)

    # Calculate duration in hours
    duration_hours = float(str(distance_miles / speed_mph)[:4])

    # Calculate calories burned using the correct formula
    calories_burned = math.ceil(met_value * weight_kg * duration_hours)

    # Health and wellness message
    default_message = (
        " As always, stay hydrated and check in with your body to ensure that you "
        "aren't exacerbating any pre-existing pain points. Remember, it is generally "
        "better to stay active rather than cease activity due to worry of worsening your symptoms."
    )

    # Conditional final message
    if calories_burned <= 200:
        return (
            f"You burned {int(calories_burned)} calories; that was a decent exercise."
            + default_message
        )
    elif calories_burned <= 400:
        return (
            f"Woah, you burned {int(calories_burned)} calories; looks like you're on a mission."
            + default_message
        )
    else:
        return (
            f"Okay... you burned {int(calories_burned)} calories on a {distance_miles} mile walk; "
            "that's a lot of expenditure! Unless you're on a serious journey, go have some recovery food. "
            "Make sure to consume a light snack containing electrolytes and proteins..."
            + default_message
        )

def get_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Please enter a positive value.\n")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a numeric value.\n")

def get_activity_met_and_speed():
    print("\nPlease select your activity level:")
    print("1. Walking (3.0 mph) - MET 3.5")
    print("2. Walking (4.0 mph) - MET 5.0")
    print("3. Hiking (4.5 mph) - MET 7.5")
    print("4. Running (5.0 mph) - MET 8.3")
    print("5. Running (6.0 mph) - MET 9.8")


    activity_met_values = {
        '1': {'met': 3.5, 'speed_mph': 3.0},
        '2': {'met': 5.0, 'speed_mph': 4.0},
        '3': {'met': 7.5, 'speed_mph': 4.5},
        '4': {'met': 8.3, 'speed_mph': 5.0},
        '5': {'met': 9.8, 'speed_mph': 6.0},
    }

    while True:
        choice = input("Enter the number corresponding to your activity: ")
        if choice in activity_met_values:
            met = activity_met_values[choice]['met']
            speed = activity_met_values[choice]['speed_mph']
            return met, speed

        else:
            print("Invalid choice. Please select a number from 1 to 5.\n")

# Run functionality in order

def main():
    print("Welcome to the Calorie Burn Calculator!\n")

    weight = get_float_input("Enter your weight in pounds: ")
    distance = get_float_input("Enter the distance hiked in miles: ")
    met_value, speed_mph = get_activity_met_and_speed()

    result = calculate_calories_burned(weight, distance, met_value, speed_mph)

    print("\n" + result)

if __name__ == "__main__":
    main()