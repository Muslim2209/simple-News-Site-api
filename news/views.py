from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from news.models import News, NewsTag, NewsCategory, Comment
from news.permissions import IsAdminOrReadOnly
from news.serializers import (
    NewsSerializer, NewsCategorySerializer,
    NewsTagSerializer, CommentSerializer,
    CommentCreateSerializer)


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    # def get_permissions(self):
    #     permission_classes = []
    #     if self.action in ['create']:
    #         permission_classes = [
    #             IsAuthenticated
    #         ]
    #     return [permission() for permission in permission_classes]


class NewsTagViewSet(viewsets.ModelViewSet):
    queryset = NewsTag.objects.all()
    serializer_class = NewsTagSerializer
    permission_classes = [IsAdminOrReadOnly]


class NewsCategoryViewSet(viewsets.ModelViewSet):
    queryset = NewsCategory.objects.all()
    serializer_class = NewsCategorySerializer
    permission_classes = [IsAdminOrReadOnly]


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()

    def get_permissions(self):
        permission_classes = []
        if self.action in ['create']:
            permission_classes = [
                IsAuthenticated
            ]
        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
        serializer_class = CommentSerializer
        if self.action in ['list', 'retrieve']:
            serializer_class = CommentSerializer
        elif self.action in ['create', 'update', 'partial_update']:
            serializer_class = CommentCreateSerializer
        return serializer_class
