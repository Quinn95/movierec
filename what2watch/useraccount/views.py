from django.shortcuts import render
from django.http import HttpResponse

from . import forms
# Create your views here.

def profile_settings(request):

    return HttpResponse(user.__str__())
