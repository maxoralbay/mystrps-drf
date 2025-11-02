from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CompanyViewSet, OfficeViewSet, CompanyOwnerViewSet

router = DefaultRouter()
router.register(r"companies", CompanyViewSet, basename="company")
router.register(r"offices", OfficeViewSet, basename="office")
router.register(r"company-owners", CompanyOwnerViewSet, basename="company-owner")

urlpatterns = [
    path("", include(router.urls)),
]

