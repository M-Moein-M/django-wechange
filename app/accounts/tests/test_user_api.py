from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User


USER_CREATE_URL = reverse('user-create')


class TestUserApi(TestCase):
    """Test user related api"""

    def setUp(self):
        self.client = APIClient()

    def test_creating_new_user_api(self):
        payload = {
            'username': 'test-username',
            'email': 'test-email@test.com',
            'password': 'test-passwd'
        }
        res = self.client.post(USER_CREATE_URL, payload)
        user = User.objects.filter(email=payload['email'])

        self.assertEqual(status.HTTP_201_CREATED, res.status_code)
        self.assertTrue(user.exists())
