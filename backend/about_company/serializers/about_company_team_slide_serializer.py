from rest_framework import serializers

from ..models import AboutCompanyTeamSlide


class AboutCompanyTeamSlideSerializer(serializers.ModelSerializer):
    """Сериализатор слайда команды."""

    class Meta:
        model = AboutCompanyTeamSlide
        fields = (
            "id",
            "big_image",
            "small_image",
            "background_image",
            "year",
            "full_name",
            "description",
        )
