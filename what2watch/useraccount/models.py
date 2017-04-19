from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User




# https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html#onetoone


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    liked_movies = models.ManyToManyField('movierec.Movie',
                                          related_name='liked')
    disliked_movies = models.ManyToManyField('movierec.Movie',
                                             related_name='disliked')

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

