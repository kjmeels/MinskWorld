from drf_spectacular.utils import extend_schema
from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import GenericViewSet

from .filters import ApartmentFilter
from .models import Apartment
from .serializers import ApartmentSerializer


@extend_schema(tags=["Properties"])
class PropertyViewSet(ListModelMixin, GenericViewSet):
    # filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ApartmentFilter

    serializer_class = ApartmentSerializer

    queryset = Apartment.objects.all()
