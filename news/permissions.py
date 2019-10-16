from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, obj, *args, **kwargs):
        if request.method in permissions.SAFE_METHODS or request.user.is_superuser:
            return True
        return False
