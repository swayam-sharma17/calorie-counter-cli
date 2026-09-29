"""Tests for input validation."""

import unittest
from calorie_counter.exceptions import ValidationError
from calorie_counter.validators import InputValidator

class TestInputValidator(unittest.TestCase):
    def test_valid_text(self) -> None:
        self.assertEqual(InputValidator.text("  Swayam  ", "Name"), "Swayam")

    def test_empty_text(self) -> None:
        with self.assertRaises(ValidationError):
            InputValidator.text("", "Name")

    def test_positive_float(self) -> None:
        self.assertEqual(InputValidator.positive_float("72.5", "Weight"), 72.5)

    def test_negative_float(self) -> None:
        with self.assertRaises(ValidationError):
            InputValidator.positive_float("-1", "Weight")

    def test_integer_range(self) -> None:
        self.assertEqual(InputValidator.integer("20", "Age", 1, 120), 20)

    def test_integer_outside_range(self) -> None:
        with self.assertRaises(ValidationError):
            InputValidator.integer("121", "Age", 1, 120)

    def test_gender(self) -> None:
        self.assertEqual(InputValidator.gender("m"), "m")

    def test_invalid_gender(self) -> None:
        with self.assertRaises(ValidationError):
            InputValidator.gender("X")

    def test_activity_choice(self) -> None:
        self.assertEqual(InputValidator.activity_choice("3"), "3")

    def test_invalid_activity_choice(self) -> None:
        with self.assertRaises(ValidationError):
            InputValidator.activity_choice("9")

if __name__ == "__main__":
    unittest.main()
