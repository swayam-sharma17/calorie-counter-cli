"""Tests for calculation logic."""

import unittest
from calorie_counter.calculator import CalorieCalculator
from calorie_counter.exceptions import ValidationError

class TestCalorieCalculator(unittest.TestCase):
    def test_male_bmr(self) -> None:
        self.assertEqual(
            CalorieCalculator.calculate_bmr(70, 175, 20, "M"),
            1688.75,
        )

    def test_female_bmr(self) -> None:
        self.assertEqual(
            CalorieCalculator.calculate_bmr(60, 165, 20, "F"),
            1320.25,
        )

    def test_tdee(self) -> None:
        self.assertEqual(CalorieCalculator.calculate_tdee(1688.75, 1.2), 2026.5)

    def test_food_calories(self) -> None:
        self.assertEqual(CalorieCalculator.calculate_food_calories(130, 200), 260.0)

    def test_total_calories(self) -> None:
        self.assertEqual(CalorieCalculator.total_calories([100, 250.5, 49.5]), 400.0)

    def test_invalid_bmr(self) -> None:
        with self.assertRaises(ValidationError):
            CalorieCalculator.calculate_bmr(0, 175, 20, "M")

if __name__ == "__main__":
    unittest.main()
