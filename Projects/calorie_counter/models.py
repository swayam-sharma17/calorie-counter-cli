"""Typed data models used by the application."""

from __future__ import annotations
from dataclasses import asdict, dataclass, field
from typing import Any

@dataclass
class Profile:
    """User profile and calculated energy information."""
    name: str
    weight_kg: float
    height_cm: float
    age: int
    gender: str
    activity: str
    bmr: float
    tdee: float

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "Profile":
        return cls(
            name=str(data["name"]),
            weight_kg=float(data["weight_kg"]),
            height_cm=float(data["height_cm"]),
            age=int(data["age"]),
            gender=str(data["gender"]),
            activity=str(data["activity"]),
            bmr=float(data["bmr"]),
            tdee=float(data["tdee"]),
        )

@dataclass
class FoodEntry:
    """Represents one food entry."""
    food: str
    calories: float
    grams: float | None = None

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "FoodEntry":
        grams = data.get("grams")
        return cls(
            food=str(data["food"]),
            calories=float(data["calories"]),
            grams=float(grams) if grams is not None else None,
        )

@dataclass
class ApplicationData:
    """Root persistence model."""
    profile: Profile | None = None
    logs: dict[str, list[FoodEntry]] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return {
            "profile": self.profile.to_dict() if self.profile else None,
            "logs": {
                day: [entry.to_dict() for entry in entries]
                for day, entries in self.logs.items()
            },
        }

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "ApplicationData":
        raw_profile = data.get("profile")
        profile = (
            Profile.from_dict(raw_profile)
            if isinstance(raw_profile, dict)
            else None
        )

        raw_logs = data.get("logs", {})
        logs: dict[str, list[FoodEntry]] = {}

        if isinstance(raw_logs, dict):
            for day, entries in raw_logs.items():
                if isinstance(entries, list):
                    logs[str(day)] = [
                        FoodEntry.from_dict(entry)
                        for entry in entries
                        if isinstance(entry, dict)
                    ]

        return cls(profile=profile, logs=logs)
