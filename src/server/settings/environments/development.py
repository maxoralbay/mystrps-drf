from os import getenv

FORCE_SCRIPT_NAME = getenv("FORCE_SCRIPT_NAME", "")

SECRET_KEY = getenv("SECRET_KEY", "django-insecure-dev-key-change-in-production")
DEBUG = getenv("DEBUG", "True").lower() == "true"
ALLOWED_HOSTS = getenv("ALLOWED_HOSTS", "*").split(",")

