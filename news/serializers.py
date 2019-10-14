from djoser.serializers import UserCreateSerializer
from rest_framework import serializers

from news.models import News, NewsCategory, NewsTag, CustomUser


class CustomUserSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = UserCreateSerializer.Meta.model
        fields = UserCreateSerializer.Meta.fields


class NewsTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsTag
        fields = '__all__'


class NewsCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsCategory
        fields = '__all__'


class NewsSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    category = NewsCategorySerializer(many=False)
    tag = NewsTagSerializer()

    class Meta:
        model = News
        fields = '__all__'  # ['id', 'title', 'body', 'author']

    def create(self, validated_data):
        category_data = validated_data.pop('category')
        category = NewsCategory(**category_data)
        if category is not None:
            category.save()
        tag_data = validated_data.pop('tag')
        tag = NewsTag(**tag_data)
        if tag is not None:
            tag.save()
        news = News(category=category, tag=tag, **validated_data)
        news.save()
        return news
