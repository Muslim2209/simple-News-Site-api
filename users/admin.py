from django.contrib import admin
from django.contrib.auth.models import Permission

from users.models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['email', 'first_name', 'last_name', 'is_subscribed']
    list_filter = ['email', 'is_subscribed']


admin.site.register(Permission)
