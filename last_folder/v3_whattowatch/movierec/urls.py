from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^home/$', views.home, name="home"),
    url(r'^form/$', views.recView, name="recommendations"),
    url(r'^search$', views.search, name='search'),
]
