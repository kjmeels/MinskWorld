from django.db.models import Prefetch
from drf_spectacular.utils import extend_schema
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet

from properties.models import Building
from .models import Project
from .serializers import ProjectSerializer, ProjectDetailSerializer


@extend_schema(tags=["Projects"])
class ProjectViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin):
    """Вьюсет проектов."""

    def get_serializer_class(self):
        if self.action == "list":
            return ProjectSerializer
        if self.action == "retrieve":
            return ProjectDetailSerializer

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
