from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema_view, extend_schema

from companies.models import Company
from companies.api.v1.serializers.company import (
    CompanySerializer,
    CompanyCreateUpdateSerializer,
)
from utils.permissions import IsAuthenticatedOrLocal

@extend_schema_view(
    list=extend_schema(description="List all companies"),
    retrieve=extend_schema(description="Retrieve a company"),
    create=extend_schema(description="Create a new company"),
    update=extend_schema(description="Update a company"),
    partial_update=extend_schema(description="Partially update a company"),
    destroy=extend_schema(description="Delete a company"),
)
class CompanyViewSet(viewsets.ModelViewSet):
    """ViewSet for managing companies."""

    queryset = Company.objects.all()
    permission_classes = [IsAuthenticatedOrLocal]
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    search_fields = ["name", "legal_name", "company_code"]
    ordering_fields = ["name", "created", "foundation_date"]
    ordering = ["name"]

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update"]:
            return CompanyCreateUpdateSerializer
        return CompanySerializer

