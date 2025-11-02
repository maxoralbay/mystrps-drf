from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema_view, extend_schema

from companies.models import Office
from companies.api.v1.serializers.office import OfficeSerializer
from utils.permissions import IsAuthenticatedOrLocal


@extend_schema_view(
    list=extend_schema(description="List all offices"),
    retrieve=extend_schema(description="Retrieve an office"),
    create=extend_schema(description="Create a new office"),
    update=extend_schema(description="Update an office"),
    partial_update=extend_schema(description="Partially update an office"),
    destroy=extend_schema(description="Delete an office"),
)
class OfficeViewSet(viewsets.ModelViewSet):
    """ViewSet for managing offices."""

    queryset = Office.objects.select_related("company").all()
    serializer_class = OfficeSerializer
    permission_classes = [IsAuthenticatedOrLocal]
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    search_fields = ["name", "company__name", "address"]
    ordering_fields = ["name", "created"]
    ordering = ["-is_main_office", "name"]
    filterset_fields = ["company", "is_main_office", "is_active"]

