"""
Calorie Counter - Vityarthhi Project
A command-line calorie tracking application built in Python.
Features:
 - BMR/TDEE calculation (Mifflin-St Jeor equation)
 - Food database with calories per 100g
 - Daily food logging
 - Progress tracking against a calorie goal
 - Persistent storage using JSON
"""

import json
import os
from datetime import date

DATA_FILE = "calorie_data.json"

FOOD_DB ={
    "rice (cooked)": 130,
    "roti": 120,
    "dal": 116,
    "paneer": 265,
    "chicken breast": 165,
    "egg": 155,
    "banana": 89,
    "apple": 52,
    "milk": 42,
    "curd": 60,
    "bread slice": 265,
    "peanut butter": 588,
    "almonds": 579,
    "potato": 77,
    "chapati oil": 884,
    "tea (with milk & sugar)": 40,
}


def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {"profile": {}, "logs": {}}


def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)


def calculate_bmr(weight_kg, height_cm, age, gender):
    if gender.lower().startswith("m"):
        return 10 * weight_kg + 6.25 * height_cm - 5 * age + 5
    else:
        return 10 * weight_kg + 6.25 * height_cm - 5 * age - 161


ACTIVITY_MULTIPLIERS = {
    "1": ("Sedentary (little/no exercise)", 1.2),
    "2": ("Lightly active (1-3 days/week)", 1.375),
    "3": ("Moderately active (3-5 days/week)", 1.55),
    "4": ("Very active (6-7 days/week)", 1.725),
    "5": ("Extra active (athlete/physical job)", 1.9),
}


def setup_profile(data):
    print("\n--- Set Up Your Profile ---")
    name = input("Name: ")
    weight = float(input("Weight (kg): "))
    height = float(input("Height (cm): "))
    age = int(input("Age: "))
    gender = input("Gender (M/F): ")

    print("\nActivity Level:")
    for key, (label, _) in ACTIVITY_MULTIPLIERS.items():
        print(f"  {key}. {label}")
    activity_choice = input("Choose (1-5): ")
    activity_label, multiplier = ACTIVITY_MULTIPLIERS.get(
        activity_choice, ACTIVITY_MULTIPLIERS["1"]
    )

    bmr = calculate_bmr(weight, height, age, gender)
    tdee = round(bmr * multiplier)

    goal = input("\nGoal - (L)ose / (M)aintain / (G)ain weight: ").lower()
    if goal.startswith("l"):
        target = tdee - 500
    elif goal.startswith("g"):
        target = tdee + 500
    else:
        target = tdee

    data["profile"] = {
        "name": name,
        "weight": weight,
        "height": height,
        "age": age,
        "gender": gender,
        "activity": activity_label,
        "bmr": round(bmr),
        "tdee": tdee,
        "target_calories": target,
    }
    save_data(data)
    print(f"\nProfile saved. Your daily calorie target is {target} kcal.\n")


def show_profile(data):
    profile = data.get("profile")
    if not profile:
        print("No profile set up yet. Choose option 1 first.")
        return
    print("\n--- Your Profile ---")
    for key, value in profile.items():
        print(f"{key.replace('_', ' ').title()}: {value}")
    print()


def log_food(data):
    today = str(date.today())
    logs = data.setdefault("logs", {})
    day_log = logs.setdefault(today, [])

    print("\n--- Log Food ---")
    print("Type 'list' to see the food database, or 'custom' for a manual entry.")
    query = input("Food name: ").strip().lower()

    if query == "list":
        for food, cal in FOOD_DB.items():
            print(f"  {food}: {cal} kcal/100g")
        return log_food(data)

    if query == "custom":
        name = input("Custom food name: ")
        calories = float(input("Total calories for this entry: "))
        day_log.append({"food": name, "calories": calories})
    elif query in FOOD_DB:
        grams = float(input(f"Quantity of '{query}' in grams: "))
        calories = round(FOOD_DB[query] * grams / 100, 1)
        day_log.append({"food": f"{query} ({grams}g)", "calories": calories})
    else:
        print("Food not found in database. Use 'custom' to add it manually.")
        return

    save_data(data)
    print(f"Logged {calories} kcal.\n")


def daily_summary(data):
    today = str(date.today())
    entries = data.get("logs", {}).get(today, [])
    target = data.get("profile", {}).get("target_calories")

    print(f"\n--- Summary for {today} ---")
    if not entries:
        print("No food logged today.\n")
        return

    total = 0
    for entry in entries:
        print(f"  {entry['food']}: {entry['calories']} kcal")
        total += entry["calories"]

    print(f"\nTotal consumed: {round(total)} kcal")
    if target:
        remaining = round(target - total)
        status = "remaining" if remaining >= 0 else "over target"
        print(f"Daily target: {target} kcal")
        print(f"{abs(remaining)} kcal {status}")
    print()


def main_menu():
    data = load_data()
    while True:
        print("===== VITYARTHHI CALORIE COUNTER =====")
        print("1. Set up / update profile")
        print("2. View profile")
        print("3. Log food")
        print("4. View today's summary")
        print("5. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            setup_profile(data)
        elif choice == "2":
            show_profile(data)
        elif choice == "3":
            log_food(data)
        elif choice == "4":
            daily_summary(data)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")


if __name__ == "__main__":
    main_menu()