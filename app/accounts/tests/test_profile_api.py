from django.test import TestCase
from django.contrib.auth.models import User
from core.models import Profile

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