from django.contrib.auth.models import Permission, Group
from rest_framework import viewsets

from admin_page.serializers import PermissionSerializer, GroupSerializer


class PermissionViewSet(viewsets.ModelViewSet):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
