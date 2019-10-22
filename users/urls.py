from django.conf.urls import url
from rest_framework import routers
from django.urls import path, include
from users import views

# router = routers.DefaultRouter()
# router.register(r'', views.NewsViewSet)


urlpatterns = [
    # path('', include(router.urls)),
    url(r'^auth/users/activation/(?P<uid>[\w-]+)/(?P<token>[\w-]+)/$', views.UserActivationView.as_view()),
    url(r'^auth/users/unsubscribe/(?P<uid>[\w-]+)/(?P<token>[\w-]+)/$', views.UnsubscribeView.as_view()),
]
