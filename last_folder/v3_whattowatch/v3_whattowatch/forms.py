from django import forms
import account.forms


STREAMING_CHOICES = (
    ('netflix', 'Netflix'),
    ('amazon', 'Amazon Prime'),
    ('hulu', 'Hulu'),
)

class SignupForm(account.forms.SignupForm):
    
    streaming_services = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=STREAMING_CHOICES,
        )