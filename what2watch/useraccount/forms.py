from django import forms
from movierec.models import Movie

LANGUAGE_CHOICES = (("English", "en"))

class ProfileForm(forms.Form):
    display_name = forms.CharField(label="Display name", max_length=20,
                                   required=True)
    languages = forms.MultipleChoiceField(
        required=True,
        widget=forms.CheckboxSelectedMultiple,
        choices=LANGUAGE_CHOICES
    )
    liked_movies = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectedMultiple,
        queryset=Movie.object.all()
    )

