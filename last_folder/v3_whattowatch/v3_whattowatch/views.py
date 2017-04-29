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
		profile.save()

	def after_signup(self, form):
		self.update_profile(form)
		super(SignupView, self).after_signup(form)