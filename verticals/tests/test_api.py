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


class TestRootAPIView(APITestCase):
    def test_root_api_view(self):
        url = reverse('api_root')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TestAdvertsAPIListView(APITestCase):
    def test_advert_list_api_view(self):
        url = reverse('api_adverts_list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TestCategoriesAPIListView(APITestCase):
    def test_categories_list_api_view(self):
        url = reverse('api_categories_list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

