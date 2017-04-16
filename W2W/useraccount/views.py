from django.shortcuts import render

from account.views import SignupView as SignupViewBase

# Create your views here.


class SignupView(SignupViewBase):
    def __init__(self):
        super(self)
