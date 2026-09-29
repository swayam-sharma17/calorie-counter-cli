"""Input validation utilities."""

from __future__ import annotations
import math
from datetime import date

from calorie_counter.constants import MAX_FOOD_NAME_LENGTH, MAX_NAME_LENGTH
from calorie_counter.exceptions import ValidationError

class InputValidator:
    """Validates user-provided values."""

    @staticmethod
    def text(value: str, field_name: str, max_length: int = MAX_NAME_LENGTH) -> str:
        cleaned = value.strip()
        if not cleaned:
            raise ValidationError(f"{field_name} cannot be empty.")
        if len(cleaned) > max_length:
            raise ValidationError(
                f"{field_name} must be {max_length} characters or fewer."
            )
        return cleaned

    @staticmethod
    def positive_float(value: str, field_name: str) -> float:
        try:
            number = float(value)
        except ValueError as exc:
            raise ValidationError(f"{field_name} must be a number.") from exc
        if not math.isfinite(number) or number <= 0:
            raise ValidationError(f"{field_name} must be greater than zero.")
        return number

    @staticmethod
    def bounded_float(value: str, field_name: str, minimum: float, maximum: float) -> float:
        number = InputValidator.positive_float(value, field_name)
        if not minimum <= number <= maximum:
            raise ValidationError(
                f"{field_name} must be between {minimum} and {maximum}."
            )
        return number

    @staticmethod
    def integer(value: str, field_name: str, minimum: int, maximum: int) -> int:
        try:
            number = int(value)
        except ValueError as exc:
            raise ValidationError(f"{field_name} must be an integer.") from exc
        if not minimum <= number <= maximum:
            raise ValidationError(
                f"{field_name} must be between {minimum} and {maximum}."
            )
        return number

    @staticmethod
    def gender(value: str) -> str:
        cleaned = value.strip().lower()
        if cleaned not in {"m", "f"}:
            raise ValidationError("Gender must be M or F.")
        return cleaned

    @staticmethod
    def activity_choice(value: str) -> str:
        cleaned = value.strip()
        if cleaned not in {"1", "2", "3", "4", "5"}:
            raise ValidationError("Activity level must be between 1 and 5.")
        return cleaned

    @staticmethod
    def food_name(value: str) -> str:
        return InputValidator.text(value, "Food name", MAX_FOOD_NAME_LENGTH)

    @staticmethod
    def date_string(value: str) -> str:
        try:
            parsed = date.fromisoformat(value)
        except ValueError as exc:
            raise ValidationError("Date must use YYYY-MM-DD format.") from exc
        return parsed.isoformat()
