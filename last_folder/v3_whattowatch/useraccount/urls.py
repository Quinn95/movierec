from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^settings/$', views.profile_settings, name='profile_settings')
]
