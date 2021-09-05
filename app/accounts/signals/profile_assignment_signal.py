from django.db.models.signals import post_save
from core.models import Profile
from django.contrib.auth.models import User


def assign_profile_to_user(sender, **kwargs):
    instance, created = kwargs['instance'], kwargs['created']
    if created:
        Profile.objects.create(user=instance)


post_save.connect(receiver=assign_profile_to_user,
                  sender=User,
                  dispatch_uid='d1360173792e0e24d48deb')
