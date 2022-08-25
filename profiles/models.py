from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django_countries.fields import CountryField


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                blank=False, related_name='profile')
    default_phone_number = models.CharField(max_length=20, null=True, blank=True)
    default_street_address1 = models.CharField(max_length=80, null=True, blank=True)
    default_street_address2 = models.CharField(max_length=80, null=True,blank=True)
    default_town_or_city = models.CharField(max_length=40, null=True, blank=True)
    default_county = models.CharField(max_length=80, null=True,blank=True)
    default_postcode = models.CharField(max_length=20, null=True,blank=True)
    default_country = CountryField(blank_label="Country", null=True, blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """
    On creation of a new user account a profile will
    also be made so that the user can easily have a profile
    automatically made for them
    """
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    """
    Alows the user profile to be saved on changes
    """
    instance.profile.save()
