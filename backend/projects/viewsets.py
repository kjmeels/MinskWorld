from drf_spectacular.utils import extend_schema
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from .models import Project
from .serializers import ProjectSerializer


@extend_schema(tags=["Projects"])
class ProjectViewSet(GenericViewSet):
    """Вьюсет проектов."""

    def get_serializer_class(self):
        if self.action == "get_projects":
            return ProjectSerializer

    def get_queryset(self):
        if self.action == "get_projects":
            return Project.objects.all().select_related("metro_station", "metro_station__line")

    @action(detail=False, methods=["GET"])
    def get_projects(self, request):
        """Эндпоинт получения списка проектов"""
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
