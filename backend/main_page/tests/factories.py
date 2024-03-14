from factory.django import DjangoModelFactory
import factory

from main_page.models import MainPageTopSlide


class MainPageTopSlideFactory(DjangoModelFactory):
    head_text = factory.Faker("word")
    body_text = factory.Faker("word")
    image = factory.django.ImageField(filename="test.png")
    order = factory.Sequence(lambda x: x + 1)

    class Meta:
        model = MainPageTopSlide
