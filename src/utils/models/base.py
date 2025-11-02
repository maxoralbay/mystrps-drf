from uuid import uuid4

from django.db import models
from simple_history.models import HistoricalRecords


class BaseModel(models.Model):
    """Base class for common fields and methods."""

    id = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid4,
        verbose_name="ID",
    )
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class HistoryModel(models.Model):
    """Model with historical records for audit trail."""

    history = HistoricalRecords(
        custom_model_name=lambda x: f"Audit{x}",
        inherit=True,
    )

    class Meta:
        abstract = True

    @property
    def _history_user(self):
        return None

    @_history_user.setter
    def _history_user(self, value):
        pass
