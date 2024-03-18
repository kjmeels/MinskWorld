from rest_framework import serializers

from ..models import ApartmentSelection


class ApartmentSelectionSerializer(serializers.ModelSerializer):
    """Сериализатор подборки квартир."""

    class Meta:
        model = ApartmentSelection
        fields = (
            "id",
            "category_name",
            "image",
        )
