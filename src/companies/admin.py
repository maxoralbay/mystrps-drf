from django.contrib import admin
from .models import Company, CompanyOwner, Office


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ("name", "legal_name", "company_code", "status", "created")
    list_filter = ("status", "created")
    search_fields = ("name", "legal_name", "company_code")
    date_hierarchy = "created"


@admin.register(CompanyOwner)
class CompanyOwnerAdmin(admin.ModelAdmin):
    list_display = ("company", "user", "created")
    list_filter = ("created",)
    search_fields = ("company__name", "user__username")


@admin.register(Office)
class OfficeAdmin(admin.ModelAdmin):
    list_display = ("name", "company", "is_main_office", "is_active", "created")
    list_filter = ("is_main_office", "is_active", "created")
    search_fields = ("name", "company__name")

