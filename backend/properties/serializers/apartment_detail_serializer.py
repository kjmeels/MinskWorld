from rest_framework import serializers

from ..models import Apartment


class ApartmentDetailSerializer(serializers.ModelSerializer):
    """Сериализатор деталки квартиры."""

    project_name = serializers.CharField(source="project.name")
    building_name = serializers.CharField(source="building.name")
    floor_number = serializers.CharField(source="floor.number")
    building_completion_quarter = serializers.CharField(source="building.completion_quarter")
    building_completion_year = serializers.CharField(source="building.completion_year")
    building_max_floor = serializers.IntegerField(source="max_floor")

    class Meta:
        model = Apartment
        fields = (
            "id",
            "area",
            "room_count",
            "building_completion_year",
            "building_completion_quarter",
            "project_name",
            "building_name",
            "floor_number",
            "building_max_floor",
            "number",
            "price",
            "original_price",
            "discount",
            "price_per_meter",
            "furnish",
        )
