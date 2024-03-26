from django_filters import CharFilter
from django_filters.rest_framework import FilterSet

from .models import Apartment


class ApartmentFilter(FilterSet):
    project = CharFilter(field_name="project")

    class Meta:
        model = Apartment
        fields = ["project"]
