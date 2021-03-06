from base import *

DEBUG = True

INSTALLED_APPS.append("debug_toolbar")

MIDDLEWARE.append("debug_toolbar.middleware.DebugToolbarMiddleware")

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
SITE_URL = "https://rz-we-are-social-staging.herokuapp.com/"
if DEBUG:
    PAYPAL_NOTIFY_URL = "http://rz-we-are-social-staging.herokuapp.com/a-very-hard-to-guess-url/"
PAYPAL_RECEIVER_EMAIL = "robinzigmond@gmail.com"
