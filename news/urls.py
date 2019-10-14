from django.conf.urls import url
from rest_framework import routers
from django.urls import path, include
from news import views

router = routers.DefaultRouter()
router.register(r'news', views.NewsViewSet)
router.register(r'tags', views.NewsTagViewSet)
router.register(r'categories', views.NewsCategoryViewSet)
router.register(r'comments', views.CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    url(r'^auth/users/activation/(?P<uid>[\w-]+)/(?P<token>[\w-]+)/$', views.UserActivationView.as_view()),
    url(r'^auth/users/unsubscribe/(?P<uid>[\w-]+)/(?P<token>[\w-]+)/$', views.UnsubscribeView.as_view()),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('auth/', include('djoser.urls.jwt')),
]
