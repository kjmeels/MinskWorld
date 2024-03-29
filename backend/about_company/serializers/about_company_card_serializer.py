from rest_framework import serializers

from ..models import AboutCompanyCard


class AboutCompanyCardSerializer(serializers.ModelSerializer):
    """Сериализатор карточки 'О компании'."""

    class Meta:
        model = AboutCompanyCard
        fields = (
            "id",
            "head_title",
            "body_title",
        )
