from django import forms

STREAMING_CHOICES = (("netflix", "Netflix"), ("amazon", "Amazon"), ("hulu",
                                                                    "Hulu"))

class RecForm(forms.Form):
    people = forms.CharField(label="Peple", max_length=100, required=False)
    title = forms.CharField(label="Title", max_length=100, required=False)
    streaming_services = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=STREAMING_CHOICES
    )





