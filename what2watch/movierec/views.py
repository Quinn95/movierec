from django.shortcuts import render
from django.http import HttpResponse

from utils import gbox
from utils import apiwrapper

from . import forms

# Create your views here.

def index(request):
    gbox.testing()
    return HttpResponse("Hello, world. You're at the polls index.")

def recView(request):
    if request.method == 'POST':
        form = forms.RecForm(request.POST)
        if form.is_valid():
            results = apiwrapper.processRequest(form.cleaned_data)
            return render(request, 'movierec/getrec.html', {'results': results})
    else:
        form = forms.RecForm

    return render(request, 'movierec/getrec.html', {'form': form})

