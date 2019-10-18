from django.urls import path, include
from rest_framework import routers

from admin_page import views

router = routers.DefaultRouter()
router.register(r'groups', views.GroupViewSet)
router.register(r'permissions', views.PermissionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
