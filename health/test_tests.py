from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from .models import CustomUser, Category, Data


class CustomUserTest(APITestCase):
    def test_create_user(self):
        url = reverse('create_user')
        data = {
            'username': 'testuser',
            'email': 'mesh@gmail.com',
            'location': 'Nairobi',
            'address': 'Nairobi',
            'phone': '0712345678',
            'role': 'Doctor',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(CustomUser.objects.count(), 1)