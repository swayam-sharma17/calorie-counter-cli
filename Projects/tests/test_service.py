"""Tests for application services."""

import unittest
from datetime import date

from calorie_counter.exceptions import FoodNotFoundError, ValidationError
from calorie_counter.models import ApplicationData
from calorie_counter.service import FoodService, ProfileService, SummaryService

class TestProfileService(unittest.TestCase):
    def test_create_profile(self) -> None:
        profile = ProfileService().create_profile(
            "Test User", 70, 175, 20, "M", "3"
        )
        self.assertEqual(profile.name, "Test User")
        self.assertGreater(profile.bmr, 0)
        self.assertGreater(profile.tdee, profile.bmr)

    def test_invalid_profile(self) -> None:
        with self.assertRaises(ValidationError):
            ProfileService().create_profile("", 70, 175, 20, "M", "3")

class TestFoodService(unittest.TestCase):
    def test_known_food(self) -> None:
        entry = FoodService().calculate_known_food("rice (cooked)", 200)
        self.assertEqual(entry.calories, 260)
        self.assertEqual(entry.grams, 200)

    def test_unknown_food(self) -> None:
        with self.assertRaises(FoodNotFoundError):
            FoodService().calculate_known_food("unknown food", 100)

    def test_custom_food(self) -> None:
        entry = FoodService().create_custom_entry("Homemade meal", 450)
        self.assertEqual(entry.food, "Homemade meal")
        self.assertEqual(entry.calories, 450)

    def test_daily_entry_limit(self) -> None:
        service = FoodService()
        data = ApplicationData()
        entry = service.create_custom_entry("Food", 100)

        for _ in range(200):
            service.add_entry(data, entry, date(2026, 9, 29))

        with self.assertRaises(ValidationError):
            service.add_entry(data, entry, date(2026, 9, 29))

class TestSummaryService(unittest.TestCase):
    def test_summary_without_profile(self) -> None:
        data = ApplicationData()
        service = FoodService()
        entry = service.create_custom_entry("Meal", 300)
        service.add_entry(data, entry, date(2026, 9, 29))

        summary = SummaryService().get_daily_summary(data, date(2026, 9, 29))

        self.assertEqual(summary["total_calories"], 300)
        self.assertIsNone(summary["reference_calories"])

if __name__ == "__main__":
    unittest.main()
