from django_filters import CharFilter, ChoiceFilter
from django_filters.rest_framework import FilterSet

from .constants import MortgageChoices


class MortgageFilter(FilterSet):
    bank = CharFilter(label="Фильтр по банку", field_name="bank__name")
    type = ChoiceFilter(choices=MortgageChoices.choices)
