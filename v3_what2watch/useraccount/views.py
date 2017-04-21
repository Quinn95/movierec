from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

from . import models
from . import forms

# Create your views here.

def profile_settings(request):
    user = request.user
    if user.__str__() == "AnonymousUser":
        return HttpResponse("Must be logged in")

    else:
        profile = get_object_or_404(models.Profile, user=user)
        form = forms.ProfileForm(instance=profile)
        if request.method == 'POST':
            form = forms.ProfileForm(request.POST)
            if form.is_valid():
                #change settings/etc
               # profile.disliked_movies = form.disliked_movies
                profile.liked_movies = form.cleaned_data['liked_movies']
                profile.disliked_movies = form.cleaned_data['disliked_movies']
                profile.save()
                return render(request, 'useraccount/profile_settings.html',
                              {"user": user, "form": form})


        return render(request, 'useraccount/profile_settings.html', {"user": user,
                                                                     "form": form}
                    )






