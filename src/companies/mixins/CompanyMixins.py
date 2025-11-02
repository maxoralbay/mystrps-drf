from users.models import User

class CompanyOwnerMixin:
    """Mixin for company owner."""

    def get_owner(self, obj):
        """Get company owner."""
        user = User.objects.filter(is_active=True).first()
        
        if not user:
            return None

        return {
            "id": user.id,
            "username": user.username,
            "email": user.email
        }