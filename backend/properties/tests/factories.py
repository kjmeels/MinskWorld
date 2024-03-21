from factory import SubFactory, fuzzy
from factory.django import DjangoModelFactory
import factory

from projects.tests.factories import ProjectFactory
from properties.constants import QuartersChoices, StatusChoices, RoomsCountChoices
from properties.models import Entrance, Building, Floor, Apartment


class BuildingFactory(DjangoModelFactory):
    project = SubFactory(ProjectFactory)
    name = factory.Faker("word")
    number = factory.Faker("pyint", min_value=1)
    address = factory.Faker("word")
    completion_year = factory.Faker("pyint", min_value=2020, max_value=2050)
    completion_quarter = fuzzy.FuzzyChoice(choices=QuartersChoices.values)

    class Meta:
        model = Building


class EntranceFactory(DjangoModelFactory):
    building = SubFactory(BuildingFactory)
    number = factory.Faker("pyint", min_value=1)

    class Meta:
        model = Entrance


class FloorFactory(DjangoModelFactory):
    entrance = SubFactory(EntranceFactory)
    number = factory.Faker("pyint", min_value=1)
    apartment_count = factory.Faker("pyint", min_value=1)

    class Meta:
        model = Floor


class ApartmentFactory(DjangoModelFactory):
    project = SubFactory(ProjectFactory)
    building = SubFactory(BuildingFactory)
    entrance = SubFactory(EntranceFactory)
    floor = SubFactory(FloorFactory)
    number = factory.Sequence(lambda x: x + 1)
    price = factory.Faker("pydecimal", left_digits=12, right_digits=2)
    original_price = factory.Faker("pydecimal", left_digits=12, right_digits=2)
    discount = factory.Faker("pyint", min_value=1)
    price_per_meter = factory.Faker("pydecimal", left_digits=8, right_digits=2)
    area = factory.Faker("pydecimal", left_digits=3, right_digits=2)
    class_name = factory.Faker("word")
    furnish = False
    room_count = fuzzy.FuzzyChoice(choices=RoomsCountChoices.values)
    status = StatusChoices.FREE

    class Meta:
        model = Apartment
