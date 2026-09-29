"""Secure JSON persistence layer."""

from __future__ import annotations
import json
import logging
import os
import tempfile
from pathlib import Path

from calorie_counter.constants import MAX_FILE_SIZE_BYTES
from calorie_counter.exceptions import StorageError
from calorie_counter.models import ApplicationData

LOGGER = logging.getLogger(__name__)

class JsonRepository:
    """Loads and atomically saves application data as JSON."""

    def __init__(self, data_file: str | Path) -> None:
        self.data_file = Path(data_file)

    def load(self) -> ApplicationData:
        if not self.data_file.exists():
            return ApplicationData()

        try:
            if self.data_file.stat().st_size > MAX_FILE_SIZE_BYTES:
                raise StorageError("Data file exceeds the permitted size.")

            with self.data_file.open("r", encoding="utf-8") as file:
                raw_data = json.load(file)

            if not isinstance(raw_data, dict):
                raise StorageError("Data file has an invalid root structure.")

            return ApplicationData.from_dict(raw_data)
        except (OSError, json.JSONDecodeError, KeyError, TypeError, ValueError) as exc:
            LOGGER.exception("Unable to load application data.")
            raise StorageError("Unable to load saved application data.") from exc

    def save(self, data: ApplicationData) -> None:
        """Atomically save application state."""
        self.data_file.parent.mkdir(parents=True, exist_ok=True)
        temporary_path: Path | None = None

        try:
            serialized = json.dumps(
                data.to_dict(),
                indent=2,
                ensure_ascii=False,
            )

            with tempfile.NamedTemporaryFile(
                mode="w",
                encoding="utf-8",
                dir=self.data_file.parent,
                delete=False,
            ) as temporary_file:
                temporary_file.write(serialized)
                temporary_file.flush()
                os.fsync(temporary_file.fileno())
                temporary_path = Path(temporary_file.name)

            temporary_path.replace(self.data_file)
        except OSError as exc:
            LOGGER.exception("Unable to save application data.")
            if temporary_path is not None:
                temporary_path.unlink(missing_ok=True)
            raise StorageError("Unable to save application data.") from exc
