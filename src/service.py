from client import EmailValidator
from storage import DataStorage


class EmailService:
    """Service class to handle email validation and storing results."""

    def __init__(self, api_key: str) -> None:
        self.email_validator = EmailValidator(api_key)
        self.storage = DataStorage()

    def validate_and_store(self, email: str) -> dict:
        """Validates the email and stores the result."""
        validation_result = self.email_validator.validate_email(email)
        self.storage.save_data(email, validation_result)
        return validation_result
