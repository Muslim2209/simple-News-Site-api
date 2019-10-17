import requests
from django.utils import timezone
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from news.models import News, NewsTag, NewsCategory, Comment
from news.permissions import IsAdminOrReadOnly
from news.serializers import (
    NewsSerializer, NewsCategorySerializer,
    NewsTagSerializer, CommentSerializer,
    CommentCreateSerializer)


class UserActivationView(APIView):
    @classmethod
    def get(cls, request, uid, token):
        protocol = 'https://' if request.is_secure() else 'http://'
        web_url = protocol + request.get_host()
        post_url = web_url + "/auth/users/activation/"
        post_data = {'uid': uid, 'token': token}
        result = requests.post(post_url, data=post_data)
        return Response(result)


class UnsubscribeView(APIView):
    @classmethod
    def get(cls, request, uid, token):
        protocol = 'https://' if request.is_secure() else 'http://'
        web_url = protocol + request.get_host()
        post_url = web_url + "/auth/users/unsubscribe/"
        post_data = {'uid': uid, 'token': token}
        result = requests.post(post_url, data=post_data)
        return Response(result)


class NewsViewSet(viewsets.ModelViewSet):
    serializer_class = NewsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        queryset = News.objects.filter(is_active=True)
        if self.action == 'list':
            queryset = News.objects.filter(is_active=True, publish_time__lte=timezone.now())
        return queryset


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
