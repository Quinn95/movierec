from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

from . import models
from . import forms

import account.views
from .models import UserProfile
from .forms import SignupForm

class SignupView(account.views.SignupView):
    form_class = SignupForm

    def update_profile(self, form):
        picked = form.cleaned_data['streaming_services']
        print picked
        profile = UserProfile.objects.create(user=self.created_user)
        for element in picked:
            if element == 'netflix':
                profile.show_netflix = True
            if element == 'amazon':
                profile.show_amazon = True
            if element == 'hulu':
                profile.show_hulu = True
            if element == 'hbo':
                profile.show_hbo = True
        profile.save()

	def after_signup(self, form):
		self.update_profile(form)
		super(SignupView, self).after_signup(form)
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






