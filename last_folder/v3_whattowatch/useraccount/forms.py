from django import forms
from movierec.models import Movie

from . import models
import account.forms



STREAMING_CHOICES = (
    ('netflix', 'Netflix'),
    ('amazon', 'Amazon Prime'),
    ('hulu', 'Hulu'),
    ('hbo', 'HBO Now')
)

class SignupForm(account.forms.SignupForm):    
    streaming_services = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=STREAMING_CHOICES,
        )
# Read this:
#
# https://docs.djangoproject.com/en/1.11/ref/forms/validation/
#
LANGUAGE_CHOICES = (("english", "en"), ("test", "ts"))

