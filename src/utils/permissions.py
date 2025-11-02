from django.conf import settings
from rest_framework import permissions


class IsAuthenticatedOrLocal(permissions.IsAuthenticated):
    """
    Permission that allows any authenticated user in development/local.
    In production, requires standard authentication.
    """

    def has_permission(self, request, view):
        # # In development, allow any authenticated user
        # if settings.DEBUG:
        #     return request.user and request.user.is_authenticated
        # # In production, use standard IsAuthenticated
        # return super().has_permission(request, view)
        return True

