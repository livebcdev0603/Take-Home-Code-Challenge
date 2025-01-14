import unittest
from typing import Any, Dict

from config.settings.test import get_test_settings

InnerConfig = Dict[str, Any]
DatabaseInnerConfig = Dict[str, InnerConfig]
DatabaseConfig = Dict[str, DatabaseInnerConfig]


class TestSettings(unittest.TestCase):
    """Test settings for the application"""

    def setUp(self) -> None:
        """Setup the test by loading settings."""
        self.settings = get_test_settings()

    def test_get_test_settings(self) -> None:
        """Test the primary settings configurations"""

        # Test if DEBUG is True
        self.assertTrue(self.settings['DEBUG'])

        # Test if DATABASES is correctly set for testing
        databases = self.settings.get('DATABASES', {})
        default_db = databases.get('default', {})
        self.assertEqual(default_db.get('ENGINE'), 'django.db.backends.sqlite3')
        self.assertEqual(default_db.get('NAME'), 'db.sqlite3')

        # Test if LOGGING is set correctly
        logging = self.settings.get('LOGGING', {})
        handlers = logging.get('handlers', {})
        console_handler = handlers.get('console', {})
        self.assertEqual(console_handler.get('level'), 'DEBUG')

    def test_missing_settings(self) -> None:
        """Test missing or misconfigured settings"""

        # Check if LOGGING exists
        logging = self.settings.get('LOGGING', {})
        handlers = logging.get('handlers', {})
        self.assertIn('console', handlers)

        # Test if DATABASES section is present
        databases = self.settings.get('DATABASES', {})
        self.assertIn('default', databases)

    def test_edge_case_missing_keys(self) -> None:
        """Test if key is missing or misconfigured"""
        # Simulate missing 'DEBUG' setting
        partial_settings = {
            key: item_value for key, item_value in self.settings.items() if key != 'DEBUG'
        }
        with self.assertRaises(KeyError):
            partial_settings['DEBUG']

    def test_empty_database(self) -> None:
        """Test for an empty database configuration"""
        empty_db_settings: DatabaseConfig = {
            'DATABASES': {'default': {}}
        }
        with self.assertRaises(KeyError):
            empty_db_settings['DATABASES']['default']['ENGINE']

    def test_logging_handlers(self) -> None:
        """Test if the logging configuration contains handlers"""
        logging = self.settings.get('LOGGING', {})
        handlers = logging.get('handlers', {})
        self.assertGreater(len(handlers), 0)

    def test_database_default_keys(self) -> None:
        """Test that the default database keys are correctly set"""
        databases = self.settings.get('DATABASES', {})
        default_db = databases.get('default', {})
        self.assertIn('ENGINE', default_db)
        self.assertIn('NAME', default_db)


if __name__ == '__main__':
    unittest.main()
