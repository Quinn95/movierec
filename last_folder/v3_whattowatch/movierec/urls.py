from django.conf.urls import url
from . import views



urlpatterns = [
    url(r'^$', views.home, name = "home"),
    url(r'^form/$', views.recView, name = "recommendations"),
    url(r'^search$', views.search, name = 'search'),
    url(r'^like_dislike$', views.like_dislike, name = "like_dislike"),
]
