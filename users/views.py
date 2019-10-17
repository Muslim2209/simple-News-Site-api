from djoser.views import UserViewSet
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response


class CustomUserViewsSet(UserViewSet):
    @action(["post"], detail=True)
    def unsubscribe(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.user
        user.is_subscribed = False
        user.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_permissions(self):
        pass