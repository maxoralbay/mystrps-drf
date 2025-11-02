from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView
from django.http import JsonResponse

from .engine.views import SpectacularScalarView


def healthcheck_view(request):
    return JsonResponse({"status": "ok"})


api_v1_patterns = [
    path("users/", include("users.api.v1.urls")),
    path("companies/", include("companies.api.v1.urls")),
]

apipatterns = [
    path("v1/", include(api_v1_patterns)),
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path("docs/", SpectacularScalarView.as_view(url_name="schema"), name="swagger"),
]

urlpatterns = [
    path("health/", healthcheck_view),
    path("admin/", admin.site.urls),
    path("api/", include(apipatterns)),
]

