"""Application-specific exceptions."""

class CalorieCounterError(Exception):
    """Base exception for application errors."""

class ValidationError(CalorieCounterError):
    """Raised when user input fails validation."""

class StorageError(CalorieCounterError):
    """Raised when persistent storage cannot be read or written."""

class FoodNotFoundError(CalorieCounterError):
    """Raised when a requested food does not exist."""
