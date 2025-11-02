from rest_framework import serializers
from companies.models import Company
from utils.serializers import HistorySerializer


class CompanySerializer(HistorySerializer, serializers.ModelSerializer):
    """Serializer for listing companies."""

    class Meta:
        model = Company
        fields = (
            "id",
            "name",
            "legal_name",
            "company_code",
            "description",
            "status",
            "foundation_date",
            "industry",
            "website_url",
            "tn_parent",
            "created",
            "modified",
        )
        read_only_fields = ("id", "created", "modified")


class CompanyCreateUpdateSerializer(HistorySerializer, serializers.ModelSerializer):
    """Serializer for creating and updating companies."""

    class Meta:
        model = Company
        fields = (
            "id",
            "name",
            "legal_name",
            "company_code",
            "description",
            "status",
            "foundation_date",
            "industry",
            "website_url",
            "tn_parent",
        )
        read_only_fields = ("id",)

    def validate(self, attrs):
        """Validate that a company cannot be its own parent."""
        instance = self.instance
        tn_parent = attrs.get("tn_parent")
        if instance and tn_parent:
            if tn_parent == instance:
                raise serializers.ValidationError("Company cannot be its own parent.")
            if instance in tn_parent.get_ancestors():
                raise serializers.ValidationError("Company cannot be parent of its ancestor.")
        return attrs

