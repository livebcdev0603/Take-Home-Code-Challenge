def get_test_settings() -> dict:
    """Returns test settings for the application."""
    return {
        'DEBUG': True,
        'DATABASES': {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': 'db.sqlite3',
            }
        },
        'LOGGING': {
            'version': 1,
            'disable_existing_loggers': False,
            'handlers': {
                'console': {
                    'level': 'DEBUG',
                    'class': 'logging.StreamHandler',
                },
            },
            'loggers': {
                'django': {
                    'handlers': ['console'],
                    'level': 'DEBUG',
                    'propagate': True,
                },
            },
        },
    }
