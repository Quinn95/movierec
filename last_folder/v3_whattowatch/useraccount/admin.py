from django.contrib import admin

# Register your models here.


from .models import Profile, UserProfile

admin.site.register(Profile)

admin.site.register(UserProfile)
