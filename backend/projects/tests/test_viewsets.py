from functools import partial

from pytest import mark
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from metro.tests.factories import MetroLineFactory, MetroStationFactory
from projects.tests.factories import (
    ProjectFactory,
    ProjectAdvantagesBlockFactory,
    ProjectAdvantageFactory,
)
from properties.constants import RoomsCountChoices, StatusChoices
from properties.tests.factories import BuildingFactory, ApartmentFactory


@mark.django_db
class TestProjectViewSet(APITestCase):
    def setUp(self):
        self.list_url: str = reverse("projects-list")
        self.detail_url = partial(reverse, "projects-detail")
        self.get_project_advantages_block_url: str = reverse(
            "projects-get-project-advantages-block"
        )

    def test_list(self):
        metro_lines = [MetroLineFactory() for _ in range(2)]
        metro_stations = [MetroStationFactory(line=line) for line in metro_lines for _ in range(5)]
        projects = [
            ProjectFactory(metro_station=metro_stations[_]) for _ in range(len(metro_stations))
        ]

        with self.assertNumQueries(1):
            res = self.client.get(self.list_url)

        res_json = res.json()
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res_json), len(projects))
        self.assertEqual(res_json[0]["metro_station"]["line_color"], metro_lines[0].color)

    def test_retrieve(self):
        project = ProjectFactory()
        buildings = [BuildingFactory(project=project) for _ in range(4)]
        apartments = [
            ApartmentFactory(
                building=building,
                room_count=RoomsCountChoices.values[_],
                price=1_000_000 + 100_000 * _,
                status=apart_status,
                furnish=[True, False][_ % 2],
            )
            for building in buildings
            for apart_status in StatusChoices.values
            for _ in range(7)
        ]

        with self.assertNumQueries(2):
            res = self.client.get(self.detail_url(kwargs={"pk": project.pk}))

        res_json = res.json()
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res_json["buildings"]), len(buildings))
        res_json_building = res_json["buildings"][0]
        self.assertEqual(res_json_building["has_furnish"], True)
        self.assertEqual(res_json_building["completion_quarter"], buildings[0].completion_quarter)
        self.assertEqual(res_json_building["completion_year"], buildings[0].completion_year)
        self.assertEqual(res_json_building["studio_min_price"], apartments[0].price)
        self.assertEqual(res_json_building["one_room_min_price"], apartments[1].price)
        self.assertEqual(res_json_building["two_room_min_price"], apartments[2].price)
        self.assertEqual(res_json_building["three_room_min_price"], apartments[3].price)
        self.assertEqual(res_json_building["four_room_min_price"], apartments[4].price)
        self.assertEqual(res_json_building["five_room_min_price"], apartments[5].price)
        self.assertEqual(res_json_building["six_room_min_price"], apartments[6].price)
        self.assertEqual(
            res_json_building["count_free_apartments"],
            len(apartments) / len(StatusChoices.values) / len(buildings),
        )

    def test_get_project_advantages_block(self):
        projects = [ProjectFactory() for _ in range(2)]
        block = ProjectAdvantagesBlockFactory()
        advantages = [
            ProjectAdvantageFactory(advantages_block=block, project=project)
            for project in projects
            for _ in range(3)
        ]

        with self.assertNumQueries(2):
            res = self.client.get(
                self.get_project_advantages_block_url, data={"project_id": projects[0].id}
            )

        res_json = res.json()
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res_json["project_advantages"]), len(advantages) / len(projects))
