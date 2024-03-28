from django.db.models import Prefetch, Max
from drf_spectacular.utils import extend_schema
from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import GenericViewSet

from .filters import ApartmentFilter
from .models import Apartment, Floor
from .serializers import ApartmentSerializer


@extend_schema(tags=["Properties"])
class PropertyViewSet(ListModelMixin, GenericViewSet):
    """Вьюсет квартир."""

    filterset_class = ApartmentFilter

    def get_serializer_class(self):
        if self.action == "list":
            return ApartmentSerializer

    def get_queryset(self):
        if self.action == "list":
            return (
                Apartment.objects.all()
                .select_related("floor", "project", "building")
                .annotate_max_floor()
            )
