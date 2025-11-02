from rest_framework import viewsets

from users.api.v1.serializers.user import UserSerializer
from users.models import User
from utils.permissions import IsAuthenticatedOrLocal


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet for viewing user information."""

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticatedOrLocal]

    def get_queryset(self):
        """Return the current user's information."""
        if self.action == "retrieve":
            return User.objects.filter(id=self.request.user.id)
        return User.objects.filter(id=self.request.user.id)

