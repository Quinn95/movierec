from django import forms
from movierec.models import Movie

LANGUAGE_CHOICES = (("english", "en"), ("test", "ts"))

class ProfileForm(forms.Form):
    display_name = forms.CharField(label="Display name", max_length=20,
                                   required=True)
    languages = forms.MultipleChoiceField(
        required=True,
        widget=forms.CheckboxSelectMultiple,
        choices=LANGUAGE_CHOICES
    )
    liked_movies = forms.ModelMultipleChoiceField(
        queryset=Movie.objects.all(),
        required=False,
        widget=forms.SelectMultiple
    )
    disliked_movies = forms.ModelMultipleChoiceField(
        queryset=Movie.objects.all(),
        required=False,
        widget=forms.SelectMultiple
    )

