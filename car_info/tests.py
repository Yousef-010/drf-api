# from django.test import TestCase
from django.contrib.auth import get_user_model

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


from .models import Car


class CarTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        test_user = get_user_model().objects.create_user(username='tester', password='test1234')
        test_user.save()
        test_car_info = Car.objects.create(
            purchaser=test_user,
            name="test_name",
            category = 'test_category',
            price = 15,
            description="test_description",
        )
        test_car_info.save()

    def test_car_info_model(self):
        car_info = Car.objects.get(pk=1)
        self.assertEqual(str(car_info.purchaser), 'tester')
        self.assertEqual(str(car_info.name), 'test_name')
        self.assertEqual(str(car_info.description), 'test_description')

    def test_get_car_info_by_id(self):
        url = reverse("car_info_detail", args=(1,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        car_info = response.data
        self.assertEqual(car_info["name"], "test_name")
        self.assertEqual(car_info["price"], 15)
        self.assertEqual(car_info["category"], "test_category")

    def test_create_car_info(self):
        url = reverse("car_info_list")
        data = {
            'purchaser': 1,
            'name': 'test_name_2',
            'category': 'test_category_2',
            'price': 25,
            'description': "test_description_2",
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        car_info = Car.objects.all()
        self.assertEqual(len(car_info), 2)

    def test_update_car_info(self):
        url = reverse("car_info_detail", args=(1,))
        data = {
            'purchaser': 1,
            'name': 'test',
            'category': 'test',
            'price': 10,
            'description': "test",
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        car_info = Car.objects.get(id=1)
        self.assertEqual(car_info.name, data["name"])
        self.assertEqual(car_info.purchaser.id, data["purchaser"])
        self.assertEqual(car_info.description, data["description"])

    def test_delete_car_info(self):
        url = reverse("car_info_detail", args=(1,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        car_info = Car.objects.all()
        self.assertEqual(len(car_info), 0)

