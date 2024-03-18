from factory import fuzzy
from factory.django import DjangoModelFactory
import factory

from main_page.constants import ApartmentSelectionCategoriesChoices
from main_page.models import MainPageTopSlide, ApartmentSelection, RulesBlock, RulesSlide


class TopSlideFactory(DjangoModelFactory):
    head_text = factory.Faker("word")
    body_text = factory.Faker("word")
    image = factory.django.ImageField(filename="test.png")
    order = factory.Sequence(lambda x: x + 1)

    class Meta:
        model = MainPageTopSlide


class ApartmentSelectionFactory(DjangoModelFactory):
    category_name = fuzzy.FuzzyChoice(choices=ApartmentSelectionCategoriesChoices.values)
    image = factory.django.ImageField(filename="test.png")

    class Meta:
        model = ApartmentSelection


class RulesBlockFactory(DjangoModelFactory):
    title = factory.Faker("word")
    image = factory.django.ImageField(filename="test.png")

    class Meta:
        model = RulesBlock

    @classmethod
    def _create(cls, model_class: RulesBlock, *args, **kwargs):
        if model_class.objects.exists():
            return model_class.objects.first()
        obj = model_class(*args, **kwargs)
        obj.save()
        return obj


class RulesSlideFactory(DjangoModelFactory):
    title = factory.Faker("word")
    short_description = factory.Faker("sentence")
    description = factory.Faker("paragraph")
    block = factory.SubFactory(RulesBlockFactory)

    class Meta:
        model = RulesSlide
