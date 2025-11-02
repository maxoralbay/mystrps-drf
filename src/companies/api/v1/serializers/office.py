from rest_framework import serializers
from companies.models import Office
from utils.serializers import HistorySerializer


class OfficeSerializer(HistorySerializer, serializers.ModelSerializer):
    """Serializer for offices."""

    company_name = serializers.CharField(source="company.name", read_only=True)

    class Meta:
        model = Office
        fields = (
            "id",
            "name",
            "company",
            "company_name",
            "address",
            "is_main_office",
            "is_active",
            "created",
            "modified",
        )
        read_only_fields = ("id", "created", "modified")

