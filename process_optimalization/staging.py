import os
import sys

import dj_database_url
from django.core.management.utils import get_random_secret_key

from process_optimalization.settings import *  # type: ignore  # noqa

SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", get_random_secret_key())
ALLOWED_HOSTS = os.getenv("DJANGO_ALLOWED_HOSTS", "127.0.0.1,localhost").split(",")
DEBUG = True
DEVELOPMENT_MODE = os.getenv("DEVELOPMENT_MODE", "False") == "True"

HOST_USER = os.getenv("HOST_USER")
HOST_PASSWORD = os.getenv("HOST_PASSWORD")
MAILGUN_API_KEY = os.getenv("MAILGUN_API_KEY")
MAILGUN_SENDER_DOMAIN = os.getenv("MAILGUN_SENDER_DOMAIN")

ANYMAIL = {
    "MAILGUN_API_KEY": MAILGUN_API_KEY,
    "MAILGUN_SENDER_DOMAIN": MAILGUN_SENDER_DOMAIN,
}
EMAIL_BACKEND = "anymail.backends.mailgun.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_HOST_USER = HOST_USER
EMAIL_HOST_PASSWORD = HOST_PASSWORD
EMAIL_USE_TLS = True
SERVER_EMAIL = HOST_USER
DEFAULT_FROM_EMAIL = HOST_USER



if len(sys.argv) > 0 and sys.argv[1] != "collectstatic":
    if os.getenv("DATABASE_URL", None) is None:
        raise Exception("DATABASE_URL environment variable not defined")
    DATABASES = {
        "default": dj_database_url.parse(os.environ.get("DATABASE_URL")),
    }

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")  # type: ignore  # noqa
DEVELOPER_MODE = False

CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_ALLOW_ALL = True


RENDER_EXTERNAL_HOSTNAME = os.environ.get("RENDER_EXTERNAL_HOSTNAME")

if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)

if not DEBUG:  # Tell Django to copy statics to the `staticfiles` directory
    # in your application directory on Render.
    STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")  # type: ignore  # noqa
    # Turn on WhiteNoise storage backend that takes care of compressing static files
    # and creating unique names for each version so they can safely be cached forever.
    STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

