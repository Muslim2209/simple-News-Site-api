from django.urls import path, include
from rest_framework import routers

from news import views

router = routers.DefaultRouter()
router.register(r'tags', views.NewsTagViewSet)
router.register(r'categories', views.NewsCategoryViewSet)
router.register(r'comments', views.CommentViewSet)
router.register(r'news', views.NewsViewSet, base_name='News')

urlpatterns = [
    path('', include(router.urls)),
]
