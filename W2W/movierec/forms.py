from django import forms

STREAMING_CHOICES = ("netflix", "amazon", "hulu")

class RecForm(forms.Form):
    streaming_services = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=STREAMING_CHOICES
    )



