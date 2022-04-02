from dataclasses import field
from django.core import validators
from django import forms

from .models import User

class Examformfillup(forms.ModelForm):
    class Meta:
        model = User
        fields = ['studentid','name', 'email', 'password']