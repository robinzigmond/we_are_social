from base import *

DEBUG = True

INSTALLED_APPS.append("debug_toolbar")

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3")
    }
}

# Stripe info:
STRIPE_PUBLISHABLE = os.getenv("STRIPE_PUBLISHABLE", "pk_test_AjjVRbuE0roWmK3bOFkTXrWl")
STRIPE_SECRET = os.getenv("STRIPE_SECRET", "sk_test_hSOzgeTqJC6jlTq12c3L9Gdq")

# PayPal Settings:
SITE_URL = "http://127.0.0.1:8000"
if DEBUG:
    PAYPAL_NOTIFY_URL = "http://d9cf6692.ngrok.io/a-very-hard-to-guess-url/"
PAYPAL_RECEIVER_EMAIL = "robinzigmond@gmail.com"
