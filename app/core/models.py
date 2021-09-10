from django.db import models
from django.contrib.auth.models import User
import os


class Profile(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    picture = models.CharField(max_length=255,
                               default=os.environ.get('DEFAULT_PROFILE_PIC'))
    about = models.CharField(max_length=1023, blank=True)

    def __str__(self):
        return self.user.username


class Skill(models.Model):
    LEVEL_CHOICES = ((i, i) for i in range(10))

    profile = models.ForeignKey(to=Profile,
                                on_delete=models.CASCADE,
                                related_name='skills',
                                related_query_name='skill')
    level = models.CharField(max_length=1,
                             choices=LEVEL_CHOICES,
                             default='0')
    name = models.CharField(max_length=255)

    def __str__(self):
        return f'{str(self.profile)}\t{self.name}\t{self.level}'
