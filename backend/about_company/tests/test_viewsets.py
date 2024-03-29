from django.urls import reverse
from pytest import mark

from rest_framework import status
from rest_framework.test import APITestCase

from about_company.tests.factories import (
    AboutCompanyFactory,
    AboutCompanyCardFactory,
    AboutCompanyTeamSlideFactory,
)


@mark.django_db
class TestAboutCompanyViewSet(APITestCase):
    def setUp(self):
        self.list_url: str = reverse("about_company-list")
        self.get_cards_list_url: str = reverse("about_company-get-cards-list")
        self.get_team_slide_list: str = reverse("about_company-get-team-slide-list")

    def test_list(self):
        info = AboutCompanyFactory()

        with self.assertNumQueries(1):
            res = self.client.get(self.list_url)

        res_json = res.json()
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_get_cards_list(self):
        cards = [AboutCompanyCardFactory() for _ in range(4)]

        with self.assertNumQueries(1):
            res = self.client.get(self.get_cards_list_url)

        res_json = res.json()
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res_json), len(cards))

    def test_get_team_slide_list(self):
        slides = [AboutCompanyTeamSlideFactory() for _ in range(4)]

        with self.assertNumQueries(1):
            res = self.client.get(self.get_team_slide_list)

        res_json = res.json()
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res_json), len(slides))
