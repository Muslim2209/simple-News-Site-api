from django.contrib import admin
from news.models import CustomUser, News, NewsCategory, NewsTag

admin.site.register(CustomUser)
admin.site.register(NewsTag)
admin.site.register(News)
admin.site.register(NewsCategory)
