"""Core application services."""

from __future__ import annotations
from datetime import date
from typing import Final

from calorie_counter.calculator import CalorieCalculator
from calorie_counter.constants import ACTIVITY_MULTIPLIERS, FOOD_DATABASE, MAX_DAILY_ENTRIES
from calorie_counter.exceptions import FoodNotFoundError, ValidationError
from calorie_counter.models import ApplicationData, FoodEntry, Profile
from calorie_counter.validators import InputValidator

class ProfileService:
    """Manages profile creation and energy calculations."""

    def create_profile(
        self,
        name: str,
        weight_kg: float,
        height_cm: float,
        age: int,
        gender: str,
        activity_choice: str,
    ) -> Profile:
        validated_name = InputValidator.text(name, "Name")
        validated_weight = InputValidator.bounded_float(str(weight_kg), "Weight", 1, 500)
        validated_height = InputValidator.bounded_float(str(height_cm), "Height", 30, 300)
        validated_age = InputValidator.integer(str(age), "Age", 1, 120)
        validated_gender = InputValidator.gender(gender)
        validated_activity = InputValidator.activity_choice(activity_choice)

        activity_label, multiplier = ACTIVITY_MULTIPLIERS[validated_activity]
        bmr = CalorieCalculator.calculate_bmr(
            validated_weight,
            validated_height,
            validated_age,
            validated_gender,
        )
        tdee = CalorieCalculator.calculate_tdee(bmr, multiplier)

        return Profile(
            name=validated_name,
            weight_kg=validated_weight,
            height_cm=validated_height,
            age=validated_age,
            gender=validated_gender.upper(),
            activity=activity_label,
            bmr=round(bmr, 1),
            tdee=tdee,
        )

class FoodService:
    """Manages food lookup and daily food entries."""

    food_database: Final[dict[str, float]] = FOOD_DATABASE

    def list_foods(self) -> dict[str, float]:
        return dict(self.food_database)

    def calculate_known_food(self, food_name: str, grams: float) -> FoodEntry:
        normalized = food_name.strip().lower()
        if normalized not in self.food_database:
            raise FoodNotFoundError(f"Food '{food_name}' was not found.")

        validated_grams = InputValidator.bounded_float(
            str(grams), "Quantity", 0.1, 100000
        )
        calories = CalorieCalculator.calculate_food_calories(
            self.food_database[normalized],
            validated_grams,
        )

        return FoodEntry(
            food=normalized,
            grams=validated_grams,
            calories=calories,
        )

    def create_custom_entry(self, food_name: str, calories: float) -> FoodEntry:
        validated_name = InputValidator.food_name(food_name)
        validated_calories = InputValidator.bounded_float(
            str(calories), "Calories", 0.1, 100000
        )
        return FoodEntry(food=validated_name, calories=validated_calories)

    def add_entry(
        self,
        data: ApplicationData,
        entry: FoodEntry,
        log_date: date | None = None,
    ) -> None:
        target_date = (log_date or date.today()).isoformat()
        entries = data.logs.setdefault(target_date, [])

        if len(entries) >= MAX_DAILY_ENTRIES:
            raise ValidationError(
                f"A maximum of {MAX_DAILY_ENTRIES} entries is allowed per day."
            )

        entries.append(entry)

class SummaryService:
    """Builds daily calorie summaries."""

    def get_daily_summary(
        self,
        data: ApplicationData,
        log_date: date | None = None,
    ) -> dict[str, object]:
        target_date = (log_date or date.today()).isoformat()
        entries = data.logs.get(target_date, [])
        total = CalorieCalculator.total_calories(
            [entry.calories for entry in entries]
        )
        reference = data.profile.tdee if data.profile else None
        remaining = (
            CalorieCalculator.remaining_calories(total, reference)
            if reference is not None
            else None
        )

        return {
            "date": target_date,
            "entries": entries,
            "total_calories": total,
            "reference_calories": reference,
            "difference_from_reference": remaining,
        }
