from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from .models import AboutCompany, AboutCompanyCard, AboutCompanyTeamSlide
from .serializers import (
    AboutCompanySerializer,
    AboutCompanyCardSerializer,
    AboutCompanyTeamSlideSerializer,
)


@extend_schema(tags=["About company"])
class AboutCompanyViewSet(GenericViewSet):
    """Вьюсет раздела 'О компании'."""

    def get_serializer_class(self):
        if self.action == "list":
            return AboutCompanySerializer
        if self.action == "get_cards_list":
            return AboutCompanyCardSerializer
        if self.action == "get_team_slide_list":
            return AboutCompanyTeamSlideSerializer

    def get_queryset(self):
        if self.action == "list":
            return AboutCompany.objects.first()
        if self.action == "get_cards_list":
            return AboutCompanyCard.objects.all()
        if self.action == "get_team_slide_list":
            return AboutCompanyTeamSlide.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(instance=queryset)
        return Response(serializer.data)

    @action(detail=False, methods=["GET"])
    def get_cards_list(self, request, *args, **kwargs):
        """Эндпоинт получения списка карточек 'О комании'."""
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=["GET"])
    def get_team_slide_list(self, request, *args, **kwargs):
        """Эндпоинт получения списка слайдов с командой проекта."""
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
