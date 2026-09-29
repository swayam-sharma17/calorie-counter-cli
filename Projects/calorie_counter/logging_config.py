"""Logging configuration."""

from __future__ import annotations
import logging
from pathlib import Path

from calorie_counter.constants import LOG_FILE

def configure_logging(log_file: str | Path = LOG_FILE) -> None:
    """Configure concise application logging."""
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        handlers=[logging.FileHandler(log_file, encoding="utf-8")],
    )
