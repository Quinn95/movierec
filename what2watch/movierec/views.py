from django.shortcuts import render
from django.http import HttpResponse

from utils import gbox
from utils import apiwrapper

from . import forms

# Create your views here.

def home(request):
    user = request.user
    return render(request, 'movierec/home.html', {'user': user, 'movies' : None})

def test(request):
    gbox.testing()
    return HttpResponse("You got 10 movies")

def recView(request):
    if request.method == 'POST':
        form = forms.RecForm(request.POST)
        if form.is_valid():
            results = apiwrapper.processRequest(form.cleaned_data)
            return render(request, 'movierec/recpage.html',
                          {'results': results,
                           'form': form,
                           'user': request.user})
    else:
        form = forms.RecForm

    return render(request, 'movierec/getrec.html', {'form': form, 'user':
                                                    request.user})

