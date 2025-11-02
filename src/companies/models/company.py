from django.db import models

from treenode.models import TreeNodeModel
from utils.models import BaseModel, HistoryModel


class Company(BaseModel, HistoryModel, TreeNodeModel):
    """Represents a company with hierarchy support."""

    class Status(models.TextChoices):
        INACTIVE = "inactive", "Inactive"
        ACTIVE = "active", "Active"
        SUSPENDED = "suspended", "Suspended"

    name = models.CharField(max_length=255)
    legal_name = models.CharField(max_length=255)
    company_code = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.ACTIVE)
    foundation_date = models.DateField(blank=True, null=True)
    industry = models.CharField(max_length=255, blank=True, null=True)
    website_url = models.URLField(blank=True, null=True)

    treenode_display_field = "name"

    class Meta(TreeNodeModel.Meta):
        verbose_name = "Company"
        verbose_name_plural = "Companies"
        ordering = ["name"]

    def __str__(self):
        return self.name

