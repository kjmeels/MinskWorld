from drf_spectacular.utils import extend_schema
from rest_framework import mixins, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from main_page.models import MainPageTopSlide
from .serializers import MainPageTopSlideSerializer


@extend_schema(tags=["Main Page"])
class MainPageViewSet(GenericViewSet):
    """Вьюсет главной страницы."""

    def get_serializer_class(self):
        if self.action == "get_top_slides":
            return MainPageTopSlideSerializer

    def get_queryset(self):
        if self.action in ["get_top_slides"]:
            return MainPageTopSlide.objects.all()

    @action(detail=False, methods=["GET"])
    def get_top_slides(self, request, *args, **kwargs):
        """Эндпоинт для получения верхнего слайдера"""
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
