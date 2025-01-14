# Email Validator SDK

This project implements a Python SDK that interacts with the Hunter.io API to validate email addresses. The SDK includes the following components:

- **HunterAPIClient**: Handles interaction with the Hunter.io email validation API.
- **InMemoryDataStorage**: Stores email validation results in memory.
- **EmailValidationService**: Provides a high-level service for email validation and result storage.

## Setup

1. Install the dependencies:
   ```bash
   pip install -r requirements.txt

2. Replace the API_KEY in main.py with your Hunter.io API key

3. Run following commands for testing
   ```bash
   flake8 .
   ```

   ```bash
   pycodestyle .
   ```

   ```bash
   mypy .
   ```

   ```bash
   isort .
   ```

   ```bash
   python -m unittest ./test.py
   coverage run -m unittest discover
   coverage report
   ```
   