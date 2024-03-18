from pytest import mark
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .factories import (
    TopSlideFactory,
    ApartmentSelectionFactory,
    RulesBlockFactory,
    RulesSlideFactory,
)


@mark.django_db
class TestMainPageViewSet(APITestCase):
    def setUp(self):
        self.get_top_slides_url: str = reverse("main_page-get-top-slides")
        self.get_apartment_selection_url: str = reverse("main_page-get-apartment-selection")
        self.get_rules_block_url: str = reverse("main_page-get-rules-block")
        self.get_rules_url: str = reverse("main_page-get-rules")

    def test_get_top_slides(self):
        slides = [TopSlideFactory() for _ in range(10)]

        with self.assertNumQueries(1):
            res = self.client.get(self.get_top_slides_url)

        res_json = res.json()
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res_json), len(slides))

    def test_get_apartment_selection(self):
        blocks = [ApartmentSelectionFactory() for _ in range(3)]

        with self.assertNumQueries(1):
            res = self.client.get(self.get_apartment_selection_url)

        res_json = res.json()
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res_json), len(blocks))

    def test_get_rules_block(self):
        block = RulesBlockFactory()
        slides = [RulesSlideFactory(block=block) for _ in range(10)]

        with self.assertNumQueries(2):
            res = self.client.get(self.get_rules_block_url)

        res_json = res.json()
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res_json["rules_slides"]), len(slides))

    def test_get_rules(self):
        slides = [RulesSlideFactory() for _ in range(10)]

        with self.assertNumQueries(1):
            res = self.client.get(self.get_rules_url)

        res_json = res.json()
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res_json), len(slides))
