from rest_framework import serializers

from main_page.models import MainPageTopSlide


class MainPageTopSlideSerializer(serializers.ModelSerializer):
    """Сериализатор верхних слайдов главной страницы."""

    class Meta:
        model = MainPageTopSlide
        fields = (
            "id",
            "head_text",
            "body_text",
            "image",
        )
