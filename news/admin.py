from django.contrib import admin

from news.models import News, NewsCategory, NewsTag, Comment

admin.site.register(NewsTag)
admin.site.register(News)
admin.site.register(NewsCategory)
admin.site.register(Comment)
