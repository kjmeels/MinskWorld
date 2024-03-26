from factory import fuzzy
from factory.django import DjangoModelFactory
import factory

from metro.tests.factories import MetroStationFactory
from projects.constants import ProjectChoices
from projects.models import Project, ProjectAdvantagesBlock, ProjectAdvantage


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


class ProjectAdvantagesBlockFactory(DjangoModelFactory):
    title = factory.Faker("word")

    class Meta:
        model = ProjectAdvantagesBlock

    @classmethod
    def _create(cls, model_class: ProjectAdvantagesBlock, *args, **kwargs):
        if model_class.objects.exists():
            return model_class.objects.first()
        obj = model_class(*args, **kwargs)
        obj.save()
        return obj


class ProjectAdvantageFactory(DjangoModelFactory):
    project = factory.SubFactory(ProjectFactory)
    advantages_block = factory.SubFactory(ProjectAdvantagesBlockFactory)
    title = factory.Faker("word")
    image = factory.django.ImageField(filename="test.png")
    description = factory.Faker("sentence")

    class Meta:
        model = ProjectAdvantage
