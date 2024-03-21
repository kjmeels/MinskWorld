from rest_framework import serializers

from ..models import Building


class BuildingSerializer(serializers.ModelSerializer):
    """Сериализатор домов."""

    has_furnish = serializers.BooleanField()
    studio_min_price = serializers.FloatField(allow_null=True)
    one_room_min_price = serializers.FloatField(allow_null=True)
    two_room_min_price = serializers.FloatField(allow_null=True)
    three_room_min_price = serializers.FloatField(allow_null=True)
    four_room_min_price = serializers.FloatField(allow_null=True)
    five_room_min_price = serializers.FloatField(allow_null=True)
    six_room_min_price = serializers.FloatField(allow_null=True)
    count_free_apartments = serializers.IntegerField()

    class Meta:
        model = Building
        fields = (
            "name",
            "has_furnish",
            "completion_quarter",
            "completion_year",
            "studio_min_price",
            "one_room_min_price",
            "two_room_min_price",
            "three_room_min_price",
            "four_room_min_price",
            "five_room_min_price",
            "six_room_min_price",
            "count_free_apartments",
        )
