from django.test import TestCase
from django.contrib.auth.models import User
from core.models import Profile
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status

import accounts.signals.profile_assignment_signal


class TestUser(TestCase):
    """Test user related actions"""

    def test_assign_profile_to_new_user(self):
        user = User.objects.create_user('test_name',
                                        email='test_email@test.com',
                                        password='test_pass')
        user_profile = Profile.objects.filter(user=user.id)
        self.assertEqual(1, len(user_profile))
        self.assertTrue(user_profile.exists())

    def test_updating_user_doesnt_create_new_profile(self):
        user = User.objects.create_user('test_name',
                                        email='test_email@test.com',
                                        password='test_pass')
        updated_name = 'test_name_updated'
        user.username = updated_name
        user.save()

        user_profile = Profile.objects.filter(user=user.id)
        self.assertEqual(1, len(user_profile))
        self.assertTrue(user_profile.exists())


class TestProfileApi(TestCase):
    """Test profile api"""

    def get_profile_detail_url(self, pk):
        return reverse('profile-detail', kwargs={'pk': pk})

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user('test_name',
                                             email='test_email@test.com',
                                             password='test_pass')

    def test_profile_update(self):
        self.assertTrue(Profile.objects.filter(user=self.user),
                        msg='Creating new user must assign profile to it')
        user_profile = Profile.objects.get(user=self.user)
        payload = {
            'about': 'Updated about-section of profile'
        }
        res = self.client.patch(self.get_profile_detail_url(user_profile.id),
                                payload)
        user_profile.refresh_from_db()

        self.assertEqual(status.HTTP_200_OK, res.status_code)
        for attr, value in payload.items():
            self.assertEqual(value, getattr(user_profile, attr))
