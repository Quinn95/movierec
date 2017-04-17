from django import forms

import models

STREAMING_CHOICES = (("netflix", "Netflix"), ("amazon", "Amazon"), ("hulu",
                                                                    "Hulu"))

class RecForm(forms.Form):
    people = forms.CharField(label="People", max_length=200, required=False)
    title = forms.CharField(label="Title", max_length=100, required=False)
    for genre in models.Genre.objects.all():
        print genre.name, genre.identifier
    streaming_services = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=STREAMING_CHOICES
    )





