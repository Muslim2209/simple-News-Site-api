from django.contrib.auth.models import Permission, Group
from rest_framework import serializers


class PermissionSerializer(serializers.ModelSerializer):
    # content_type_name = serializers.CharField(source='content_type.name', read_only=True)

    class Meta:
        model = Permission
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'
