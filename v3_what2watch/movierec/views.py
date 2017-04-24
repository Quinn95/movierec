from django.shortcuts import render
from django.http import HttpResponse

from utils import gbox, heist
from utils import apiwrapper
from .models import Person

from . import forms

# Create your views here.

def home(request):
    user = request.user
    return render(request, 'movierec/home.html', {'user': user, 'movies' : None})

def test(request):
    heist.test()
    return HttpResponse("You got movies")

def recView(request):
    if request.method == 'POST':

        return render(request, 'movierec/recpage.html',
                      {'results': results,
                       'form': form,
                       'user': request.user})
    else:
        form = forms.RecForm

    return render(request, 'movierec/recpage.html', {'form': form, 'user':
                                                    request.user, 'people': Person.objects.all()})

