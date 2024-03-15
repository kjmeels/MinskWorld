from factory import fuzzy
from factory.django import DjangoModelFactory
import factory

from metro.tests.factories import MetroStationFactory
from projects.constains import ProjectChoices
from projects.models import Project


class ProjectFactory(DjangoModelFactory):
    name = factory.Sequence(lambda x: f"Project {x}")
    slug = factory.Sequence(lambda n: f"Slug {n}")
    image = factory.django.ImageField(filename="test.png")
    description = factory.Faker("word")
    category = fuzzy.FuzzyChoice(choices=ProjectChoices.values)
    metro_station = factory.SubFactory(MetroStationFactory)
    time_to_station = factory.Faker("pyint", min_value=1, max_value=30)

    class Meta:
        model = Project
