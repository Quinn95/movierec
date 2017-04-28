from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^home/$', views.home, name="home"),
    url(r'^form/$', views.recView, name="recommendations"),
    url(r'^testing$', views.test, name='index'),
    url(r'^search$', views.search, name='search'),
]
