"""Energy and calorie calculation logic."""

from __future__ import annotations
from calorie_counter.exceptions import ValidationError

class CalorieCalculator:
    """Performs deterministic calorie-related calculations."""

    @staticmethod
    def calculate_bmr(weight_kg: float, height_cm: float, age: int, gender: str) -> float:
        if weight_kg <= 0 or height_cm <= 0 or age <= 0:
            raise ValidationError("Weight, height, and age must be positive.")

        normalized_gender = gender.lower()
        if normalized_gender.startswith("m"):
            return 10 * weight_kg + 6.25 * height_cm - 5 * age + 5
        if normalized_gender.startswith("f"):
            return 10 * weight_kg + 6.25 * height_cm - 5 * age - 161
        raise ValidationError("Gender must be M or F.")

    @staticmethod
    def calculate_tdee(bmr: float, activity_multiplier: float) -> float:
        if bmr <= 0 or activity_multiplier <= 0:
            raise ValidationError("BMR and activity multiplier must be positive.")
        return round(bmr * activity_multiplier, 1)

    @staticmethod
    def calculate_food_calories(calories_per_100g: float, grams: float) -> float:
        if calories_per_100g < 0 or grams <= 0:
            raise ValidationError(
                "Calories per 100g cannot be negative and grams must be positive."
            )
        return round(calories_per_100g * grams / 100, 1)

    @staticmethod
    def total_calories(calories: list[float]) -> float:
        return round(sum(calories), 1)

    @staticmethod
    def remaining_calories(total: float, reference: float) -> float:
        return round(reference - total, 1)
