from pytest import mark
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from main_page.tests.factories import MainPageTopSlideFactory


@mark.django_db
class TestMainPageViewSet(APITestCase):
    def setUp(self):
        self.get_top_slides_url: str = reverse("main_page-get-top-slides")

    def test_get_top_slides(self):
        slides = [MainPageTopSlideFactory() for _ in range(10)]

        with self.assertNumQueries(1):
            res = self.client.get(self.get_top_slides_url)

        res_json = res.json()
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res_json), len(slides))
