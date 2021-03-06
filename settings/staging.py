from base import *
import dj_database_url

DEBUG = False

# Logging:

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
        },
    },
}

# Load the ClearDB connection details from the environment variable
DATABASES = {
    "default": dj_database_url.config("CLEARDB_DATABASE_URL")
}

# Stripe info:
STRIPE_PUBLISHABLE = os.getenv("STRIPE_PUBLISHABLE", "pk_test_AjjVRbuE0roWmK3bOFkTXrWl")
STRIPE_SECRET = os.getenv("STRIPE_SECRET", "sk_test_hSOzgeTqJC6jlTq12c3L9Gdq")

# PayPal Settings:
SITE_URL = "https://rz-we-are-social-staging.herokuapp.com/"
PAYPAL_NOTIFY_URL = "http://rz-we-are-social-staging.herokuapp.com/a-very-hard-to-guess-url/"
PAYPAL_RECEIVER_EMAIL = "robinzigmond@gmail.com"
