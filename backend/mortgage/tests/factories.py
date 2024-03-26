import factory
from factory import fuzzy
from factory.django import DjangoModelFactory

from mortgage.constants import MortgageChoices
from mortgage.models import MortgageBank, MortgageOffer


class MortgageBankFactory(DjangoModelFactory):
    name = factory.Faker("word")
    slug = factory.Sequence(lambda n: f"Slug {n}")
    logo = factory.django.ImageField(filename="test.png")

    class Meta:
        model = MortgageBank


class MortgageOfferFactory(DjangoModelFactory):
    bank = factory.SubFactory(MortgageBankFactory)
    min_sum = factory.Faker("pyint", min_value=1)
    max_sum = factory.Faker("pyint", min_value=1)
    min_term = factory.Faker("pyint", min_value=1, max_value=30)
    max_term = factory.Faker("pyint", min_value=1, max_value=30)
    rate = factory.Faker("pyint", min_value=1, max_value=30)
    type = fuzzy.FuzzyChoice(choices=MortgageChoices.values)

    class Meta:
        model = MortgageOffer
