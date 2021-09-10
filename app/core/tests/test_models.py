from django.test import TestCase
from core.models import Profile, Skill
from django.contrib.auth.models import User


class TestProfileModel(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('test_name',
                                             email='test_email@test.com',
                                             password='test_pass')

    def test_representation(self):
        self.assertTrue(Profile.objects.filter(user=self.user),
                        msg='Creating new user must assign profile to it')
        user_profile = Profile.objects.get(user=self.user)
        self.assertEqual(self.user.username, str(user_profile))


class TestSkillModel(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('test_name',
                                             email='test_email@test.com',
                                             password='test_pass')
        self.assertTrue(Profile.objects.filter(user=self.user),
                        msg='Creating new user must assign profile to it')
        self.profile = Profile.objects.get(user=self.user)

    def test_representation(self):
        skill = Skill.objects.create(profile=self.profile,
                                     name='Python Programmer',
                                     level='5')
        expected = f'{skill.profile.user.username}\t{skill.name}\t{skill.level}'
        self.assertEqual(expected, str(skill))
