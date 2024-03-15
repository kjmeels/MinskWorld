from rest_framework import serializers

from metro.serializers import MetroStationSerializer
from .models import Project


class ProjectSerializer(serializers.ModelSerializer):
    """Сериализатор проекта."""

    metro_station = MetroStationSerializer()

    class Meta:
        model = Project
        fields = (
            "name",
            "slug",
            "image",
            "description",
            "category",
            "metro_station",
            "time_to_station",
        )
