from factory.django import DjangoModelFactory
import factory

from about_company.models import AboutCompany, AboutCompanyCard, AboutCompanyTeamSlide


class AboutCompanyFactory(DjangoModelFactory):
    title = factory.Faker("word")
    head_description = factory.Faker("word")
    low_description = factory.Faker("word")
    image = factory.django.ImageField(filename="test.png")

    class Meta:
        model = AboutCompany

    @classmethod
    def _create(cls, model_class: AboutCompany, *args, **kwargs):
        if model_class.objects.exists():
            return model_class.objects.first()
        obj = model_class(*args, **kwargs)
        obj.save()
        return obj


class AboutCompanyCardFactory(DjangoModelFactory):
    head_title = factory.Faker("word")
    body_title = factory.Faker("word")

    class Meta:
        model = AboutCompanyCard


class AboutCompanyTeamSlideFactory(DjangoModelFactory):
    big_image = factory.django.ImageField(filename="test.png")
    small_image = factory.django.ImageField(filename="test.png")
    background_image = factory.django.ImageField(filename="test.png")
    year = factory.Faker("pyint", min_value=2010)
    full_name = factory.Faker("word")
    description = factory.Faker("word")
    order = factory.Sequence(lambda x: x + 1)

    class Meta:
        model = AboutCompanyTeamSlide
