from os import getenv

STATIC_URL = "static/"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": getenv("POSTGRES_DB", "drf"),
        "USER": getenv("POSTGRES_USER", "postgres"),
        "PASSWORD": getenv("POSTGRES_PASSWORD", "postgres"),
        "HOST": getenv("POSTGRES_HOST", "localhost"),
        "PORT": getenv("POSTGRES_PORT", "5432"),
        "CONN_HEALTH_CHECKS": getenv("POSTGRES_CONN_HEALTH_CHECKS", "True").lower() == "true",
        "CONN_MAX_AGE": int(getenv("POSTGRES_CONN_MAX_AGE", "300")),
    }
}

