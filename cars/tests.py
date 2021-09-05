import json

from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Car, Rate

class CreateCarTestCase(APITestCase):
    
    def test_cars_list(self):
        response = self.client.get("/cars/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_car_creation(self):
        data = {'make':'Volkswagen','model': 'Golf'}
        response = self.client.post("/cars/", data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_duplicate_car_creation(self):
        data = {'make':'Volkswagen','model': 'Golf'}
        self.client.post("/cars/", data, format='json')
        response = self.client.post("/cars/", data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['non_field_errors'][0], "The fields make, model must make a unique set.")

    def test_incorrect_make_car_creation(self):
        data = {'make':'Incorrect make','model': 'Golf'}
        response = self.client.post("/cars/", data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['non_field_errors'][0], "The make does not exist.")
    
    def test_incorrect_model_car_creation(self):
        data = {'make':'Volkswagen','model': 'Incorrect model'}
        response = self.client.post("/cars/", data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['non_field_errors'][0], "The model does not exist.")
            

class DeleteCarTestCase(APITestCase):

    def setUp(self):
        self.car = Car.objects.create(make='Volkswagen',model='Golf')

    def test_car_deletion(self):
        response = self.client.delete(f"/cars/{self.car.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_non_existent_car_deletion(self):
        response = self.client.delete("/cars/110/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class RateCarTestCase(APITestCase):

    def setUp(self):
        self.golf = Car.objects.create(make='Volkswagen',model='Golf')
    
    def test_car_rate(self):
        data = {"car_id": 1, "rating": 5}
        response = self.client.post("/rate/", data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_non_existent_car_rate(self):
        data = {"car_id": 110, "rating": 5}
        response = self.client.post("/rate/", data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_rating_too_high_range_car_rate(self):
        data = {"car_id": 1, "rating": 6}
        response = self.client.post("/rate/", data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_rating_too_low_range_car_rate(self):
        data = {"car_id": 1, "rating": 0}
        response = self.client.post("/rate/", data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class CarListsTestCase(APITestCase):

    def setUp(self):
        self.golf = Car.objects.create(make='Volkswagen',model='Golf')
        self.passat = Car.objects.create(make='Volkswagen',model='Passat')

        for _ in range(20):
            Rate.objects.create(car_id=self.golf,rating=5)
        
        for _ in range(15):
            Rate.objects.create(car_id=self.passat,rating=3)

    def test_popular_car_list(self):
        response = self.client.get("/popular/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(dict(response.data[0]), {"id": 1,"make": "Volkswagen", "model": "Golf", "rates_number": 20})
        self.assertEqual(dict(response.data[1]), {"id": 2,"make": "Volkswagen", "model": "Passat", "rates_number": 15})

    def test_car_list(self):
        response = self.client.get("/cars/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(dict(response.data[1]), {"id": 2,"make": "Volkswagen", "model": "Passat", "avg_rating": 3.0})
        self.assertEqual(dict(response.data[0]), {"id": 1,"make": "Volkswagen", "model": "Golf", "avg_rating": 5.0})
        
