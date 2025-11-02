from os import getenv

FORCE_SCRIPT_NAME = getenv("FORCE_SCRIPT_NAME", "")

SECRET_KEY = getenv("SECRET_KEY", "test-secret-key")
DEBUG = True
ALLOWED_HOSTS = ["*"]

