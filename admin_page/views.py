from django.contrib.auth.models import Group, Permission
from rest_framework import viewsets

from admin_page.serializers import GroupSerializer, PermissionSerializer


class GroupViewSet(viewsets.ModelViewSet):
    serializer_class = GroupSerializer
    queryset = Group.objects.all()


class PermissionViewSet(viewsets.ModelViewSet):
    serializer_class = PermissionSerializer
    queryset = Permission.objects.all()
