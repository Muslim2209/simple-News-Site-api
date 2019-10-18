from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('news/', include('news.urls')),
    path('myadmin/', include('admin_page.urls')),
    path('', include('users.urls')),
]
