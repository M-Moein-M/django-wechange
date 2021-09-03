from django.test import TestCase
from core.models import Profile
from django.contrib.auth.models import User


class TestProfileModel(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('test_name',
                                             email='test_email@test.com',
                                             password='test_pass')

    def test_representation(self):
        instance = Profile.objects.create(user=self.user)
        self.assertEqual(self.user.username, str(instance))
