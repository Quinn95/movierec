from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver




# https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html#onetoone




@python_2_unicode_compatible
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    liked_movies = models.ManyToManyField('movierec.Movie',
                                          related_name='liked_movies')
    disliked_movies = models.ManyToManyField('movierec.Movie',
                                             related_name='disliked_movies')
    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


