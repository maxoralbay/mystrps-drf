from rest_framework import serializers
from companies.models import CompanyOwner
from utils.serializers import HistorySerializer


class CompanyOwnerSerializer(HistorySerializer, serializers.ModelSerializer):
    """Serializer for company owners."""

    company_name = serializers.CharField(source="company.name", read_only=True)
    user_username = serializers.CharField(source="user.username", read_only=True)

    class Meta:
        model = CompanyOwner
        fields = (
            "id",
            "company",
            "company_name",
            "user",
            "user_username",
            "created",
            "modified",
        )
        read_only_fields = ("id", "created", "modified")

