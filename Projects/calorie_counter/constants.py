"""Application constants."""

from typing import Final

APP_NAME: Final[str] = "VITyarthi Calorie Counter"
DATA_FILE: Final[str] = "calorie_data.json"
LOG_FILE: Final[str] = "calorie_counter.log"

FOOD_DATABASE: Final[dict[str, float]] = {
    "rice (cooked)": 130.0,
    "roti": 120.0,
    "dal": 116.0,
    "paneer": 265.0,
    "chicken breast": 165.0,
    "egg": 155.0,
    "banana": 89.0,
    "apple": 52.0,
    "milk": 42.0,
    "curd": 60.0,
    "bread slice": 265.0,
    "peanut butter": 588.0,
    "almonds": 579.0,
    "potato": 77.0,
    "chapati oil": 884.0,
    "tea (with milk & sugar)": 40.0,
}

ACTIVITY_MULTIPLIERS: Final[dict[str, tuple[str, float]]] = {
    "1": ("Sedentary (little/no exercise)", 1.2),
    "2": ("Lightly active (1-3 days/week)", 1.375),
    "3": ("Moderately active (3-5 days/week)", 1.55),
    "4": ("Very active (6-7 days/week)", 1.725),
    "5": ("Extra active (athlete/physical job)", 1.9),
}

MAX_NAME_LENGTH: Final[int] = 80
MAX_FOOD_NAME_LENGTH: Final[int] = 100
MAX_DAILY_ENTRIES: Final[int] = 200
MAX_FILE_SIZE_BYTES: Final[int] = 5 * 1024 * 1024
