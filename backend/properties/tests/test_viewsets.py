from django.urls import reverse
from pytest import mark
from rest_framework import status

from rest_framework.test import APITestCase

from projects.tests.factories import ProjectFactory
from properties.constants import QuartersChoices, RoomsCountChoices
from properties.tests.factories import ApartmentFactory, FloorFactory, BuildingFactory


@mark.django_db
class TestPropertyViewSet(APITestCase):
    def setUp(self):
        self.list_url: str = reverse("properties-list")

    def test_list(self):
        apartments = [ApartmentFactory(price=100_000, original_price=120_000) for _ in range(4)]

        with self.assertNumQueries(1):
            res = self.client.get(self.list_url)

            res_json = res.json()
            self.assertEqual(res.status_code, status.HTTP_200_OK)
            self.assertEqual(len(res_json), len(apartments))

    def test_area_filter(self):
        apartments = [
            ApartmentFactory(area=100 + _, price=100_000, original_price=120_000) for _ in range(4)
        ]

        with self.assertNumQueries(1):
            res = self.client.get(
                self.list_url,
                {
                    "area_min": apartments[0].area,
                    "area_max": apartments[len(apartments) // 2 - 1].area,
                },
            )

        res_json = res.json()
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res_json), len(apartments) // 2)

    def test_completion_quarter_filter(self):
        buildings = [BuildingFactory(completion_quarter=_) for _ in QuartersChoices.values]
        apartments = [
            ApartmentFactory(building=building, price=100_000, original_price=120_000)
            for building in buildings
        ]
        with self.assertNumQueries(1):
            res = self.client.get(self.list_url, {"completion_quarter": QuartersChoices.values[0]})

        res_json = res.json()
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res_json), len(apartments) / len(QuartersChoices.values))

    def test_completion_year_filter(self):
        buildings = [BuildingFactory(completion_year=2022 + _) for _ in range(4)]
        apartments = [
            ApartmentFactory(building=building, price=100_000, original_price=120_000)
            for building in buildings
        ]
        with self.assertNumQueries(1):
            res = self.client.get(self.list_url, {"completion_year": buildings[0].completion_year})

        res_json = res.json()
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res_json), len(apartments) / len(buildings))

    def test_floor_filter(self):
        floors = [FloorFactory(number=_) for _ in range(10)]
        apartments = [
            ApartmentFactory(floor=_, price=100_000, original_price=120_000) for _ in floors
        ]

        with self.assertNumQueries(1):
            res = self.client.get(
                self.list_url,
                {
                    "floor_min": apartments[0].floor.number,
                    "floor_max": apartments[len(apartments) // 2 - 1].floor.number,
                },
            )

        res_json = res.json()
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res_json), len(apartments) // 2)

    def test_price_filter(self):
        apartments = [
            ApartmentFactory(price=100_000 + _ * 1000, original_price=120_000) for _ in range(4)
        ]

        with self.assertNumQueries(1):
            res = self.client.get(
                self.list_url,
                {
                    "price_min": apartments[0].price,
                    "price_max": apartments[len(apartments) // 2 - 1].price,
                },
            )

        res_json = res.json()
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res_json), len(apartments) // 2)

    def test_project_filter(self):
        projects = [ProjectFactory() for _ in range(4)]
        apartments = [
            ApartmentFactory(
                project=_,
                price=100_000,
                original_price=120_000,
            )
            for _ in projects
        ]

        with self.assertNumQueries(1):
            res = self.client.get(self.list_url, {"project": projects[0].slug})

        res_json = res.json()
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res_json), len(apartments) / len(projects))

    def test_room_count_filter(self):
        apartments = [
            ApartmentFactory(room_count=_, price=100_000, original_price=120_000)
            for _ in RoomsCountChoices.values
        ]

        with self.assertNumQueries(1):
            res = self.client.get(self.list_url, {"room_count": RoomsCountChoices.values[0]})

        res_json = res.json()
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res_json), len(apartments) / len(RoomsCountChoices.values))
