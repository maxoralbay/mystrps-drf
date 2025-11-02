from django.urls import path
from rest_framework.routers import DefaultRouter

from users.api.v1.views.auth import RegisterView, LoginView
from users.api.v1.views.user import UserViewSet

router = DefaultRouter()
router.register(r"", UserViewSet, basename="user")

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
] + router.urls

