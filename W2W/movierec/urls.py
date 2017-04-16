from django.conf.urls import url
from . import views



urlpatterns = [
    url(r'^form/$', views.recView, name="rec"),
    url(r'^testing$', views.index, name='index')
]
