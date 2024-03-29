from rest_framework import serializers

from ..models import AboutCompany


class AboutCompanySerializer(serializers.ModelSerializer):
    """Сериализатор блока 'О компании'."""

    class Meta:
        model = AboutCompany
        fields = (
            "title",
            "head_description",
            "low_description",
            "image",
        )
