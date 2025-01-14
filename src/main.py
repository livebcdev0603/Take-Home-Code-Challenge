import logging

from service import EmailService

logging.basicConfig(level=logging.INFO)


def main() -> None:
    """Main function to run the email validation."""
    email_service = EmailService("your_api_key")
    email = "test@example.com"
    validation_result = email_service.validate_and_store(email)
    logging.info(f"Email validation result: {validation_result}")


if __name__ == "__main__":
    main()
