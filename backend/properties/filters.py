from django_filters import CharFilter, RangeFilter, ChoiceFilter
from django_filters.rest_framework import FilterSet

from .constants import RoomsCountChoices


class ApartmentFilter(FilterSet):
    project = CharFilter(field_name="project__slug")
    room_count = ChoiceFilter(choices=RoomsCountChoices.choices, label="Фильтр по комнатности")
    area = RangeFilter(field_name="area")
    price = RangeFilter(field_name="price")
    completion_year = CharFilter(field_name="building__completion_year")
    completion_quarter = CharFilter(field_name="building__completion_quarter")
    floor = RangeFilter(field_name="floor__number")
