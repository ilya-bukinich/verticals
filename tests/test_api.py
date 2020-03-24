from rest_framework.reverse import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class TestCreateAdvert(APITestCase):
    def test_create_advert(self):
        url = reverse('api_advert_create')
        data = {'title': 'Test advert', 'summary': 'Test description'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class TestCreateAdvertWithoutData(APITestCase):
    def test_create_advert(self):
        url = reverse('api_advert_create')
        data = {}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
