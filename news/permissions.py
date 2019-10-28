import copy

from rest_framework import permissions
from rest_framework.permissions import DjangoModelPermissions


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS or request.user.is_superuser:
            return True
        return False

# class CustomDjangoModelPermissions(DjangoModelPermissions):
#     def __init__(self):
#         self.perms_map = copy.deepcopy(self.perms_map)
#         self.perms_map['GET'] = ['%(app_label)s.view_%(model_name)s']
