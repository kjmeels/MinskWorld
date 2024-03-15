from rest_framework import serializers

from .models import MetroStation


class MetroStationSerializer(serializers.ModelSerializer):
    """Сериализатор станции метро."""

    line_color = serializers.CharField(source="line.color")

    class Meta:
        model = MetroStation
        fields = (
            "name",
            "line_color",
        )
