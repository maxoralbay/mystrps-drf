from django.db import models
from utils.models import BaseModel


class Office(BaseModel):
    """Company office location."""

    name = models.CharField(max_length=255)
    company = models.ForeignKey(
        "companies.Company",
        on_delete=models.CASCADE,
        related_name="offices",
    )
    address = models.TextField(blank=True, null=True)
    is_main_office = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Office"
        verbose_name_plural = "Offices"
        ordering = ["-is_main_office", "name"]

    def __str__(self):
        return f"{self.name} - {self.company.name}"

