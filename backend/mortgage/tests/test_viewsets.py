from django.urls import reverse
from pytest import mark
from rest_framework import status
from rest_framework.test import APITestCase

from mortgage.constants import MortgageChoices
from mortgage.tests.factories import MortgageBankFactory, MortgageOfferFactory


@mark.django_db
class TestMortgageViewSet(APITestCase):
    def setUp(self):
        self.list_url: str = reverse("mortgage-list")

    def test_list(self):
        offers = [
            MortgageOfferFactory(
                min_sum=100 + _, max_sum=100_000 + _ * 1000, min_term=1 + _, max_term=20 + _
            )
            for _ in range(4)
        ]

        with self.assertNumQueries(1):
            res = self.client.get(self.list_url, {"summ": "102000", "term": "22"})

            res_json = res.json()
            self.assertEqual(res.status_code, status.HTTP_200_OK)
            self.assertEqual(len(res_json), len(offers) / 2)

    def test_bank_filter(self):
        bank_names = ["Сбер", "Альфа"]
        banks = [MortgageBankFactory(name=name) for name in bank_names]
        offers = [
            MortgageOfferFactory(bank=bank, min_sum=10, max_sum=100_000, min_term=1, max_term=20)
            for bank in banks
            for _ in range(4)
        ]

        with self.assertNumQueries(1):
            res = self.client.get(
                self.list_url, {"bank": bank_names[0], "summ": "10000", "term": "10"}
            )

        res_json = res.json()
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res_json), len(offers) / len(bank_names))

    def test_type_filter(self):
        offers = [
            MortgageOfferFactory(type=_, min_sum=10, max_sum=100_000, min_term=1, max_term=20)
            for _ in MortgageChoices.values
        ]

        with self.assertNumQueries(1):
            res = self.client.get(
                self.list_url, {"type": MortgageChoices.values[0], "summ": "10000", "term": "10"}
            )

        res_json = res.json()
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res_json), len(offers) / len(MortgageChoices.values))
