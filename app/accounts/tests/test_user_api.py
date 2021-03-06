from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session

USER_CREATE_URL = reverse('user-create')
USER_LOGIN_URL = reverse('user-login')
USER_LOGOUT_URL = reverse('user-logout')


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

    def test_login_user_api(self):
        payload = {
            'username': 'test-username',
            'email': 'test-email@test.com',
            'password': 'test-passwd'
        }

        User.objects.create_user(**payload)
        res = self.client.post(USER_LOGIN_URL, payload)

        self.assertIsNotNone(
            self.client.cookies.get('sessionid'),
            msg='Login endpoint does not store cookie for session auth')
        self.assertEqual(status.HTTP_200_OK, res.status_code)

    def test_login_user_api_wrong_credentials(self):
        payload = {
            'username': 'test-username',
            'email': 'test-email@test.com',
            'password': 'test-passwd'
        }

        User.objects.create_user(**payload)

        payload['password'] = 'WRONG-PASSWORD'
        res = self.client.post(USER_LOGIN_URL, payload)

        self.assertIsNone(
            self.client.cookies.get('sessionid'),
            msg='Wrong credentials must fail login endpoint')
        self.assertEqual(status.HTTP_401_UNAUTHORIZED, res.status_code)

    def test_logout_user_api(self):
        payload = {
            'username': 'test-username',
            'email': 'test-email@test.com',
            'password': 'test-passwd'
        }

        User.objects.create_user(**payload)
        self.client.login(**payload)
        res = self.client.post(USER_LOGOUT_URL)

        self.assertEqual(
            0,
            self.client.cookies.get('sessionid').get('max-age'),
            msg='Logout must clear session')
        self.assertEqual(status.HTTP_204_NO_CONTENT, res.status_code)
