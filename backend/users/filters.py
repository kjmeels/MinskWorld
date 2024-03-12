from django_filters import rest_framework as filters

from users.constants import GenderChoices
from users.models import User


class UserFilter(filters.FilterSet):
    age = filters.RangeFilter(field_name="age")
    gender = filters.ChoiceFilter(choices=GenderChoices.choices)

    class Meta:
        model = User
        fields = ["age", "full_name"]
