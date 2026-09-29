"""Tests for persistent storage."""

import tempfile
import unittest
from pathlib import Path

from calorie_counter.models import ApplicationData, FoodEntry
from calorie_counter.repository import JsonRepository

class TestJsonRepository(unittest.TestCase):
    def test_load_missing_file_returns_empty_data(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            repository = JsonRepository(Path(directory) / "data.json")
            data = repository.load()
            self.assertIsNone(data.profile)
            self.assertEqual(data.logs, {})

    def test_save_and_load(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            repository = JsonRepository(Path(directory) / "data.json")
            data = ApplicationData(
                logs={
                    "2026-09-29": [
                        FoodEntry("rice (cooked)", 260, 200)
                    ]
                }
            )
            repository.save(data)
            loaded = repository.load()

            self.assertIn("2026-09-29", loaded.logs)
            self.assertEqual(
                loaded.logs["2026-09-29"][0].food,
                "rice (cooked)",
            )
            self.assertEqual(loaded.logs["2026-09-29"][0].calories, 260)

if __name__ == "__main__":
    unittest.main()
