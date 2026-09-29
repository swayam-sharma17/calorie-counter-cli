# VITyarthi Calorie Counter

## Overview
A modular command-line calorie tracking application written entirely in Python.

## Features
- Profile creation and updating
- BMR calculation using Mifflin-St Jeor
- TDEE/reference calculation
- Built-in food database
- Quantity-based calorie calculation
- Custom food entries
- Daily food logging
- Daily summaries
- Persistent JSON storage
- Validation and error handling
- Logging
- Unit tests

## Technology Stack
- Python 3.10+
- Python standard library
- dataclasses
- pathlib
- json
- logging
- unittest

## Installation
Install Python 3.10 or newer. No third-party dependencies are required.

Optional virtual environment:
```bash
python -m venv .venv
```

## Execution
```bash
python -m calorie_counter
```

## Testing
```bash
python -m unittest discover -s tests -v
```

## Project Structure
```text
calorie_counter/
    __init__.py
    __main__.py
    cli.py
    calculator.py
    constants.py
    exceptions.py
    logging_config.py
    models.py
    repository.py
    service.py
    validators.py

tests/
    test_calculator.py
    test_repository.py
    test_service.py
    test_validators.py
```

## Persistence and Security
Data is stored locally in JSON. The application uses validation, atomic writes, file-size limits, and no dynamic code execution or external network calls.

## Note
BMR and TDEE are mathematical estimates and are presented as reference values rather than medical advice.
