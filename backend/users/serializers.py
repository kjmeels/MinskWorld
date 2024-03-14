from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    """Сериализатор пользователей."""

    class Meta:
        model = User
        fields = (
            "id",
            "full_name",
            "image",
            "age",
            "gender",
            "birth_date",
        )
