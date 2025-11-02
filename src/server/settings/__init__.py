from os import environ

from split_settings.tools import include

environ.setdefault("DJANGO_ENV", "development")
_ENV = environ["DJANGO_ENV"]

_base_settings = (
    "components/common.py",
    "components/i18n.py",
    "components/celery.py",
    "components/security.py",
    "components/storage.py",
    # Select the right env:
    "environments/{0}.py".format(_ENV),
    "components/caches.py",
)

include(*_base_settings)

