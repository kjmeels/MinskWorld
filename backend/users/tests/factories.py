import factory
from factory import fuzzy
from factory.django import DjangoModelFactory

from ..constants import GenderChoices
from ..models import User


class UserFactory(DjangoModelFactory):
    username = factory.Sequence(lambda x: f"user_{x}")
    full_name = factory.Faker("word")
    image = factory.django.ImageField(filename="test.png")
    age = factory.Faker("pyint", min_value=0, max_value=99)
    gender = fuzzy.FuzzyChoice(choices=GenderChoices.values)
    birth_date = factory.Faker("date")

    class Meta:
        model = User


