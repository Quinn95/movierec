from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver




# https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html#onetoone

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    show_netflix = models.BooleanField(default=False)
    show_amazon = models.BooleanField(default=False)
    show_hulu = models.BooleanField(default=False)
    show_hbo = models.BooleanField(default=False)

    def __str__(self):
         return self.user.username


