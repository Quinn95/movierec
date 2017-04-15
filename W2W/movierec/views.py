from django.shortcuts import render
from django.http import HttpResponse

from utils import gbox

# Create your views here.

def index(request):
    gbox.testing()
    return HttpResponse("Hello, world. You're at the polls index.")

