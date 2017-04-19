from django import forms
from movierec.models import Movie

from . import models

LANGUAGE_CHOICES = (("english", "en"), ("test", "ts"))

class ProfileForm(forms.ModelForm):
    class Meta:
        model = models.Profile
        fields = ("display_name", "liked_movies", "disliked_movies")

def bound_form(profile):
    form = ProfileForm(instance=profile)
    return form
