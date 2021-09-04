from django.db import models
from django.contrib.auth.models import User
import os


class Profile(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    picture = models.CharField(max_length=255,
                               default=os.environ.get('DEFAULT_PROFILE_PIC'))
    about = models.CharField(max_length=1023, blank=True)

    def __str__(self):
        return self.user.username
