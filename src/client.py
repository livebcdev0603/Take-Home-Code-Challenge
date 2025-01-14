import requests


class EmailValidator:
    """Class to validate email using the Hunter.io API."""

    def __init__(self, api_key: str):
        self.api_key = api_key

    def validate_email(self, email: str) -> dict:
        """Validates an email using Hunter.io API."""
        url = f"https://api.hunter.io/v2/email-verifier?email={email}&api_key={self.api_key}"
        response = requests.get(url)
        HTTP_OK = 200
        if response.status_code == HTTP_OK:
            return response.json()
        return {}
