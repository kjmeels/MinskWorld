from django.db.models import Prefetch
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from properties.models import Building
from .models import Project, ProjectAdvantagesBlock, ProjectAdvantage
from .serializers import (
    ProjectSerializer,
    ProjectDetailSerializer,
    ProjectAdvantagesBlockSerializer,
)


@extend_schema(tags=["Projects"])
class ProjectViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin):
    """Вьюсет проектов."""

    def get_serializer_class(self):
        if self.action == "list":
            return ProjectSerializer
        if self.action == "retrieve":
            return ProjectDetailSerializer
        if self.action == "get_project_advantages_block":
            return ProjectAdvantagesBlockSerializer

    def get_queryset(self):
        if self.action == "list":
            return Project.objects.all().select_related("metro_station", "metro_station__line")
        if self.action == "retrieve":
            return (
                Project.objects.all()
                .select_related("metro_station", "metro_station__line")
                .prefetch_related(
                    Prefetch(
                        "buildings",
                        queryset=Building.objects.all()
                        .annotate_has_furnish()
                        .annotate_studio_min_price()
                        .annotate_one_room_min_price()
                        .annotate_two_room_min_price()
                        .annotate_three_room_min_price()
                        .annotate_four_room_min_price()
                        .annotate_five_room_min_price()
                        .annotate_six_room_min_price()
                        .annotate_count_free_apartments(),
                    )
                )
            )

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="project_id", description="Id проекта", required=True, type=OpenApiTypes.INT
            )
        ]
    )
    @action(detail=False, methods=["GET"])
    def get_project_advantages_block(self, request, *args, **kwargs):
        project_advantages = ProjectAdvantage.objects.filter(
            project_id=request.query_params.get("project_id")
        )
        queryset = (
            ProjectAdvantagesBlock.objects.all()
            .prefetch_related(Prefetch("project_advantages", queryset=project_advantages))
            .first()
        )
        serializer = self.get_serializer(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)
