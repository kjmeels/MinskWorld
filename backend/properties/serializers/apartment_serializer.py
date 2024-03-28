from rest_framework import serializers

from ..models import Apartment


class ApartmentSerializer(serializers.ModelSerializer):
    """Сериализатор домов."""

    project_name = serializers.CharField(source="project.name")
    building_name = serializers.CharField(source="building.name")
    building_number = serializers.CharField(source="building.number")
    floor_number = serializers.CharField(source="floor.number")
    building_completion_quarter = serializers.CharField(source="building.completion_quarter")
    building_completion_year = serializers.CharField(source="building.completion_year")
    building_max_floor = serializers.IntegerField(source="max_floor")

    class Meta:
        model = Apartment
        fields = (
            "id",
            "project_name",
            "building_name",
            "building_number",
            "floor_number",
            "building_completion_quarter",
            "building_completion_year",
            "price",
            "original_price",
            "discount",
            "room_count",
            "area",
            "class_name",
            "building_max_floor",
        )
