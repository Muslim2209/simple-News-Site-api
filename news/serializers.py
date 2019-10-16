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

    # tag = NewsTagSerializer(many=True, required=False)

    class Meta:
        model = News
        fields = '__all__'
        # ['id', 'title', 'body', 'image', 'attachment', "created_at", "updated_at", "is_active", 'author',
        #       'comments', "category", "tag"]

    def create(self, validated_data):
        for i in validated_data:
            print(i)
            category = validated_data.pop('category')
            tags = validated_data.pop('tag')
            NewsTag.objects.get_or_create(name=tags[0])
            news = News.objects.create(**validated_data)
            news.tag = tags
            news.category = category
            return news
