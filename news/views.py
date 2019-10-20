from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, DjangoModelPermissions
from news.models import News, NewsTag, NewsCategory, Comment
from news.permissions import IsAdminOrReadOnly, CustomDjangoModelPermissions
from news.serializers import (
    NewsSerializer, NewsCategorySerializer,
    NewsTagSerializer, CommentSerializer,
    CommentCreateSerializer)


class NewsListCreateAPIView(generics.ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = [DjangoModelPermissions]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class NewsListRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = [DjangoModelPermissions]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class NewsTagViewSet(viewsets.ModelViewSet):
    queryset = NewsTag.objects.all()
    serializer_class = NewsTagSerializer
    permission_classes = [DjangoModelPermissions]


class NewsCategoryViewSet(viewsets.ModelViewSet):
    queryset = NewsCategory.objects.all()
    serializer_class = NewsCategorySerializer
    permission_classes = [DjangoModelPermissions]


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
