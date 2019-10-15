from djoser.serializers import UserCreateSerializer
from rest_framework import serializers

from news.models import News, NewsCategory, NewsTag, Comment


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


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    news = serializers.ReadOnlyField(source='news.id')

    class Meta:
        model = Comment
        fields = '__all__'


class NewsSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    comment = CommentSerializer()

    # tag = NewsTagSerializer(many=True)

    class Meta:
        model = News
        fields = '__all__'  # ['id', 'title', 'body', 'author']

    def create(self, validated_data):
        # tag_data = validated_data.pop('tag')
        # for tags tag_data:
        #     tag = NewsTag(**tags)
        #     tag.save()
        comment_data = validated_data.pop('comment')
        news = News(**validated_data)
        news.save()
        for comments in comment_data:
            comment = Comment(news=news, **comments)
            comment.save()
        return news
