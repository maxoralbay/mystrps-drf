from django.db import models
from utils.models import BaseModel


class CompanyOwner(BaseModel):
    """Company owner relationship."""

    company = models.ForeignKey(
        "companies.Company",
        on_delete=models.CASCADE,
        related_name="owners",
    )
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="owned_companies",
    )

    class Meta:
        verbose_name = "Company Owner"
        verbose_name_plural = "Company Owners"
        unique_together = [["company", "user"]]

    def __str__(self):
        return f"{self.user.username} - {self.company.name}"

