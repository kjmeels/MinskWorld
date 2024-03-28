from drf_spectacular.utils import extend_schema
from rest_framework.viewsets import ReadOnlyModelViewSet

from .filters import ApartmentFilter
from .models import Apartment
from .serializers import ApartmentSerializer, ApartmentDetailSerializer


@extend_schema(tags=["Properties"])
class PropertyViewSet(ReadOnlyModelViewSet):
    """Вьюсет квартир."""

    filterset_class = ApartmentFilter

    def get_serializer_class(self):
        if self.action == "list":
            return ApartmentSerializer
        if self.action == "retrieve":
            return ApartmentDetailSerializer

    def get_queryset(self):
        return (
            Apartment.objects.all()
            .select_related("floor", "project", "building")
            .annotate_max_floor()
        )
