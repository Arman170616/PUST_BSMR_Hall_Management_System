from dataclasses import field
from django.core import validators
from django import forms

from .models import User

class Examformfillup(forms.ModelForm):
    class Meta:
        model = User
        fields = ['studentid','name', 'email', 'password']
        #labels = {'studentid': "Enter Your StudentId", 'name': "Enter Your name" ,'password': 'Enter Your Password', 'হলের নাম': 'হলের নাম' }