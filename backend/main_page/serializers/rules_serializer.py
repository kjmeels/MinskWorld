from rest_framework import serializers

from main_page.models import RulesBlock, RulesSlide


class RulesSlideShortSerializer(serializers.ModelSerializer):
    """Короткий сериализатор слайдов с правилами."""

    class Meta:
        model = RulesSlide
        fields = (
            "id",
            "title",
            "short_description",
        )


class RulesBlockSerializer(serializers.ModelSerializer):
    """Сериализатор блока правил."""

    rules_slides = RulesSlideShortSerializer(many=True)

    class Meta:
        model = RulesBlock
        fields = ("id", "title", "image", "rules_slides")


class RulesSlideSerializer(serializers.ModelSerializer):
    """Сериализатор слайдов с правилами."""

    class Meta:
        model = RulesSlide
        fields = (
            "id",
            "title",
            "description",
        )
