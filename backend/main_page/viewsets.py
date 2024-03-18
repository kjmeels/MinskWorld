from drf_spectacular.utils import extend_schema
from rest_framework import mixins, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from .models import ApartmentSelection, MainPageTopSlide, RulesBlock, RulesSlide
from .serializers import (
    ApartmentSelectionSerializer,
    MainPageTopSlideSerializer,
    RulesBlockSerializer,
    RulesSlideSerializer,
)


@extend_schema(tags=["Main Page"])
class MainPageViewSet(GenericViewSet):
    """Вьюсет главной страницы."""

    def get_serializer_class(self):
        if self.action == "get_top_slides":
            return MainPageTopSlideSerializer
        if self.action == "get_apartment_selection":
            return ApartmentSelectionSerializer
        if self.action == "get_rules_block":
            return RulesBlockSerializer
        if self.action == "get_rules":
            return RulesSlideSerializer

    def get_queryset(self):
        if self.action in ["get_top_slides"]:
            return MainPageTopSlide.objects.all()
        if self.action == "get_apartment_selection":
            return ApartmentSelection.objects.all()
        if self.action == "get_rules_block":
            return RulesBlock.objects.all().prefetch_related("rules_slides").first()
        if self.action == "get_rules":
            return RulesSlide.objects.all()

    @action(detail=False, methods=["GET"])
    def get_top_slides(self, request, *args, **kwargs):
        """Эндпоинт для получения верхнего слайдера"""
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=["GET"])
    def get_apartment_selection(self, request, *args, **kwargs):
        """Эндпоинт получения списка подборки квартир"""
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=["GET"])
    def get_rules_block(self, request, *args, **kwargs):
        """Эндпоинт получения блока правил."""
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=["GET"])
    def get_rules(self, request, *args, **kwargs):
        """Эндпоинт получения всех правил."""
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
