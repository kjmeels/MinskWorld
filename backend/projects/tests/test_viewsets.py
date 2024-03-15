from pytest import mark
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from metro.tests.factories import MetroLineFactory, MetroStationFactory
from projects.tests.factories import ProjectFactory


@mark.django_db
class TestProjectViewSet(APITestCase):
    def setUp(self):
        self.get_projects_url: str = reverse("projects-get-projects")

    def test_get_projects(self):
        metro_lines = [MetroLineFactory() for _ in range(2)]
        metro_stations = [MetroStationFactory(line=line) for line in metro_lines for _ in range(5)]
        projects = [
            ProjectFactory(metro_station=metro_stations[_]) for _ in range(len(metro_stations))
        ]

        with self.assertNumQueries(1):
            res = self.client.get(self.get_projects_url)

        res_json = res.json()
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res_json), len(projects))
        self.assertEqual(res_json[0]["metro_station"]["line_color"], metro_lines[0].color)
