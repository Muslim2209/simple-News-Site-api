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
    author = serializers.ReadOnlyField(source='author.email')

    class Meta:
        model = Comment
        fields = '__all__'


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        exclude = ['author']

    def create(self, validated_data):
        user = None
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            user = request.user

        comment = Comment.objects.create(author=user, **validated_data)
        return comment


class NewsSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.email')
    comments = CommentSerializer(read_only=True, many=True)

    # tag = NewsTagSerializer(many=True)

    class Meta:
        model = News
        fields = '__all__'  # ['id', 'title', 'body', 'author']
