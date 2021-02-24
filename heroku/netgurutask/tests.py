from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import resolve
from django.urls import reverse
from rest_framework import status
from .models import Car
import json
from django.test import Client
# Create your tests here.
from .views import CarList

class abstrat_Test(APITestCase):
    many=True

    def json_match(self):
        serializer_data = self.Serializer(instance=self.instance.objects.all(), many=self.many).data
        response = self.client.get(self.url_test)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_data = json.loads(response.content)
        self.assertEqual(serializer_data, response_data)

    def data_match(self):
        response = self.client.get(self.url_test)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def view_match(self,view):
        self.assertEquals(resolve(self.url_test).func.view_class, view)

class CarList_test(abstrat_Test):
    url_test = reverse("cars_list", kwargs={})

    def setUp(self):
        self.client = Client()

    def test_view_match(self):
        self.view_match(CarList)

    def test_data_match(self):
        self.data_match()

    def test_add_car(self):
        data = Car.objects.create(make="BUICK", model="BUICK")
        data_post= {
            "make": "BUICK",
            "model": "nice"
        }
        response = self.client.post(self.url_test, data_post)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

