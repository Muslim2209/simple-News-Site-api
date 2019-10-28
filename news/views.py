from django.utils import timezone
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from rest_framework.response import Response

from news.models import News, NewsTag, NewsCategory, Comment
from news.serializers import (
    NewsSerializer, NewsCategorySerializer,
    NewsTagSerializer, CommentSerializer,
    CommentCreateSerializer)


class NewsViewSet(viewsets.ModelViewSet):
    serializer_class = NewsSerializer
    permission_classes = [DjangoModelPermissions]

    def get_queryset(self):
        queryset = News.objects.filter(is_active=True)
        if self.action == 'list':
            queryset = News.objects.filter(is_active=True, publish_time__lte=timezone.now())
        return queryset

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @action(["post", 'get'], detail=True)
    def subscribe(self, request, *args, **kwargs):
        news = self.get_object()
        if request.user not in news.subscribers.all():
            news.subscribers.add(request.user)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)
        news.save()
        return Response(status=status.HTTP_202_ACCEPTED)

    @action(["post", 'get'], detail=True)
    def unsubscribe(self, request, *args, **kwargs):
        news = self.get_object()
        if request.user in news.subscribers.all():
            news.subscribers.remove(request.user)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)
        news.save()
        return Response(status=status.HTTP_202_ACCEPTED)


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
