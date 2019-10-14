import requests
from djoser.views import UserViewSet
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView

from news.models import News, NewsTag, NewsCategory, Comment
from news.permissions import IsAdminOrReadOnly
from news.serializers import NewsSerializer, NewsCategorySerializer, NewsTagSerializer, CommentSerializer


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


class CustomUserViewsSet(UserViewSet):
    @action(["post"], detail=True)
    def unsubscribe(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.user
        user.is_subscribed = False
        user.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


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
    serializer_class = CommentSerializer
