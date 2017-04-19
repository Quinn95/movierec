from django.shortcuts import render
from django.http import HttpResponse

from . import forms

# Create your views here.

def profile_settings(request):
    user = request.user
    if request.method == 'POST':
        form = forms.ProfileForm(request.POST)
        if form.is_valid():
            #change settings/etc
            return render(request, 'useraccount/profile_settings.html',
                          {"user": user, "form": form})

    form = forms.ProfileForm

    return render(request, 'useraccount/profile_settings.html', {"user": user,
                                                                 "form": form}
                )






