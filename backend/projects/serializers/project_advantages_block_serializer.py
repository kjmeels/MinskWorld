from rest_framework import serializers

from ..models import ProjectAdvantagesBlock, ProjectAdvantage


class ProjectAdvantageSerializer(serializers.ModelSerializer):
    """Сериализатор преимуществ проекта."""

    class Meta:
        model = ProjectAdvantage
        fields = (
            "id",
            "title",
            "image",
            "description",
        )


class ProjectAdvantagesBlockSerializer(serializers.ModelSerializer):
    """Сериализатор преимуществ блока проекта."""

    project_advantages = ProjectAdvantageSerializer(many=True)

    class Meta:
        model = ProjectAdvantagesBlock
        fields = (
            "title",
            "project_advantages",
        )
