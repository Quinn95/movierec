from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    show_netflix = models.BooleanField(default=False)
    show_amazon = models.BooleanField(default=False)
    show_hulu = models.BooleanField(default=False)

    def __str__(self):
    	return self.user.username