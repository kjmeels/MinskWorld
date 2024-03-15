from factory.django import DjangoModelFactory
import factory

from metro.models import MetroLine, MetroStation


class MetroLineFactory(DjangoModelFactory):
    name = factory.Sequence(lambda x: f"Name {x}")
    color = factory.Faker("color")

    class Meta:
        model = MetroLine


class MetroStationFactory(DjangoModelFactory):
    name = factory.Sequence(lambda x: f"Name {x}")
    line = factory.SubFactory(MetroLineFactory)

    class Meta:
        model = MetroStation
