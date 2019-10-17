from djoser.serializers import UserCreateSerializer


class CustomUserSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = UserCreateSerializer.Meta.model
        fields = UserCreateSerializer.Meta.fields
