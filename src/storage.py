class DataStorage:
    """Data storage class to manage in-memory data."""

    def __init__(self) -> None:
        self.data_store: dict[str, dict] = {}

    def save_data(self, email: str, validation_result: dict) -> None:
        """Saves the validation result for the given email."""
        self.data_store[email] = validation_result

    def get_data(self, email: str) -> dict:
        """Retrieves the validation result for the given email."""
        return self.data_store.get(email, {})

    def delete_data(self, email: str) -> None:
        """Deletes the stored result for the given email."""
        if email in self.data_store:
            self.data_store.pop(email, None)

    def clear_all_data(self) -> None:
        """Clears all data from the storage."""
        self.data_store.clear()
