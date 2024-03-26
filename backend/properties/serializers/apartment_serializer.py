from rest_framework import serializers

from ..models import Apartment


class ApartmentSerializer(serializers.ModelSerializer):
    """Сериализатор домов."""

    class Meta:
        model = Apartment
        fields = ("id",)
