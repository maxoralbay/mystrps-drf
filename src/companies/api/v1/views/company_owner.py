from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema_view, extend_schema

from companies.models import CompanyOwner
from companies.api.v1.serializers.company_owner import CompanyOwnerSerializer
from utils.permissions import IsAuthenticatedOrLocal


@extend_schema_view(
    list=extend_schema(description="List all company owners"),
    retrieve=extend_schema(description="Retrieve a company owner"),
    create=extend_schema(description="Create a new company owner"),
    update=extend_schema(description="Update a company owner"),
    partial_update=extend_schema(description="Partially update a company owner"),
    destroy=extend_schema(description="Delete a company owner"),
)
class CompanyOwnerViewSet(viewsets.ModelViewSet):
    """ViewSet for managing company owners."""

    queryset = CompanyOwner.objects.select_related("company", "user").all()
    serializer_class = CompanyOwnerSerializer
    permission_classes = [IsAuthenticatedOrLocal]
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    search_fields = ["company__name", "user__username"]
    ordering_fields = ["created"]
    ordering = ["-created"]
    filterset_fields = ["company", "user"]

