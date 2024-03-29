from django.urls import reverse
from pytest import mark
from rest_framework import status
from rest_framework.test import APITestCase

from likes.likes import Like
from properties.tests.factories import ApartmentFactory


@mark.django_db
class LikeViewSetViewSet(APITestCase):
    def setUp(self):
        self.list_url: str = reverse("likes-list")
        self.add_like_url: str = reverse("likes-add-like")
        self.destroy_like_url: str = reverse("likes-destroy-like")
        self.clear_like_url: str = reverse("likes-clear-like")

    def test_all_methods(self):
        apartments = [ApartmentFactory(price=100_000, original_price=120_000) for _ in range(4)]

        # Проверяем, что список лайков пуст
        with self.assertNumQueries(0):
            res = self.client.get(self.list_url)

        res_json = res.json()
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res_json), 0)

        # Добавляем лайк
        with self.assertNumQueries(1):
            res = self.client.post(f"{self.add_like_url}?apartment_id={apartments[0].id}")

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

        # Проверяем, что лайк создался
        with self.assertNumQueries(0):
            res = self.client.get(self.list_url)

        res_json = res.json()
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res_json), 1)

        # Удаляем лайк
        with self.assertNumQueries(1):
            res = self.client.delete(f"{self.destroy_like_url}?apartment_id={apartments[0].id}")

        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)

        # Проверяем, что лайк удалился
        with self.assertNumQueries(0):
            res = self.client.get(self.list_url)

        res_json = res.json()
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res_json), 0)

        # Добавляем 4 лайка на каждую квартиру
        for apartment in apartments:
            self.client.post(f"{self.add_like_url}?apartment_id={apartment.id}")

        with self.assertNumQueries(0):
            res = self.client.get(self.list_url)

        res_json = res.json()
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res_json), len(apartments))

        # Чистим все лайки
        with self.assertNumQueries(0):
            res = self.client.delete(self.clear_like_url)

        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)

        # Проверяем, что список лайков пуст
        with self.assertNumQueries(0):
            res = self.client.get(self.list_url)

        res_json = res.json()
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res_json), 0)
