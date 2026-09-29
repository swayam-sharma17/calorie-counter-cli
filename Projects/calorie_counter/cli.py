"""Command-line interface."""

from __future__ import annotations
import logging
from pathlib import Path

from calorie_counter.constants import ACTIVITY_MULTIPLIERS, APP_NAME, DATA_FILE
from calorie_counter.exceptions import CalorieCounterError
from calorie_counter.logging_config import configure_logging
from calorie_counter.models import ApplicationData
from calorie_counter.repository import JsonRepository
from calorie_counter.service import FoodService, ProfileService, SummaryService

LOGGER = logging.getLogger(__name__)

class CalorieCounterCLI:
    """Interactive command-line application."""

    def __init__(self, repository: JsonRepository) -> None:
        self.repository = repository
        self.data: ApplicationData = repository.load()
        self.profile_service = ProfileService()
        self.food_service = FoodService()
        self.summary_service = SummaryService()

    def run(self) -> None:
        while True:
            self._print_menu()
            choice = input("Choose an option: ").strip()
            try:
                if choice == "1":
                    self._setup_profile()
                elif choice == "2":
                    self._show_profile()
                elif choice == "3":
                    self._log_food()
                elif choice == "4":
                    self._show_summary()
                elif choice == "5":
                    print("Goodbye!")
                    return
                else:
                    print("Invalid option. Please choose 1-5.\n")
            except CalorieCounterError as exc:
                LOGGER.warning("User operation failed: %s", exc)
                print(f"Error: {exc}\n")
            except (EOFError, KeyboardInterrupt):
                print("\nGoodbye!")
                return

    @staticmethod
    def _print_menu() -> None:
        print(f"\n===== {APP_NAME} =====")
        print("1. Set up / update profile")
        print("2. View profile")
        print("3. Log food")
        print("4. View today's summary")
        print("5. Exit")

    def _setup_profile(self) -> None:
        print("\n--- Set Up Your Profile ---")
        name = input("Name: ")
        weight = input("Weight (kg): ")
        height = input("Height (cm): ")
        age = input("Age: ")
        gender = input("Gender (M/F): ")

        print("\nActivity Level:")
        for key, (label, _) in ACTIVITY_MULTIPLIERS.items():
            print(f"  {key}. {label}")

        activity = input("Choose (1-5): ")

        try:
            profile = self.profile_service.create_profile(
                name=name,
                weight_kg=float(weight),
                height_cm=float(height),
                age=int(age),
                gender=gender,
                activity_choice=activity,
            )
        except ValueError as exc:
            raise CalorieCounterError("Numeric profile input is invalid.") from exc

        self.data.profile = profile
        self.repository.save(self.data)

        print("\nProfile saved.")
        print(f"Estimated BMR: {profile.bmr:.0f} kcal/day")
        print(f"Estimated TDEE/reference: {profile.tdee:.0f} kcal/day\n")

    def _show_profile(self) -> None:
        profile = self.data.profile
        if profile is None:
            print("\nNo profile set up yet. Choose option 1 first.\n")
            return

        print("\n--- Your Profile ---")
        print(f"Name: {profile.name}")
        print(f"Weight: {profile.weight_kg:.1f} kg")
        print(f"Height: {profile.height_cm:.1f} cm")
        print(f"Age: {profile.age}")
        print(f"Gender: {profile.gender}")
        print(f"Activity: {profile.activity}")
        print(f"Estimated BMR: {profile.bmr:.0f} kcal/day")
        print(f"Estimated TDEE/reference: {profile.tdee:.0f} kcal/day\n")

    def _log_food(self) -> None:
        print("\n--- Log Food ---")
        print("Type 'list' to view the food database.")
        print("Type 'custom' to manually enter calories.")
        query = input("Food name: ").strip().lower()

        if query == "list":
            for food, calories in self.food_service.list_foods().items():
                print(f"  {food}: {calories:.0f} kcal/100g")
            print()
            return

        try:
            if query == "custom":
                food_name = input("Custom food name: ")
                calories = float(input("Calories for this entry: "))
                entry = self.food_service.create_custom_entry(food_name, calories)
            else:
                grams = float(input(f"Quantity of '{query}' in grams: "))
                entry = self.food_service.calculate_known_food(query, grams)
        except ValueError as exc:
            raise CalorieCounterError("Numeric food input is invalid.") from exc

        self.food_service.add_entry(self.data, entry)
        self.repository.save(self.data)
        print(f"Logged {entry.calories:.1f} kcal.\n")

    def _show_summary(self) -> None:
        summary = self.summary_service.get_daily_summary(self.data)
        print(f"\n--- Summary for {summary['date']} ---")
        entries = summary["entries"]

        if not entries:
            print("No food logged today.\n")
            return

        for entry in entries:
            quantity = f" ({entry.grams:g}g)" if entry.grams else ""
            print(f"  {entry.food}{quantity}: {entry.calories:.1f} kcal")

        print(f"\nTotal consumed: {summary['total_calories']:.1f} kcal")
        reference = summary["reference_calories"]
        difference = summary["difference_from_reference"]

        if reference is not None and difference is not None:
            print(f"Estimated daily reference: {reference:.0f} kcal")
            print(f"Difference from reference: {difference:+.1f} kcal")
        print()

def main() -> None:
    """Application entry point."""
    configure_logging()
    repository = JsonRepository(Path(DATA_FILE))
    CalorieCounterCLI(repository).run()

if __name__ == "__main__":
    main()
