from unicodedata import name
from django.db import models

# Create your models here.

class User(models.Model):
    studentid = models.PositiveIntegerField()
    name = models.CharField(max_length=200, blank=True)
    email = models.EmailField(max_length=100, blank=True)
    password = models.CharField(max_length=200)
    #হলের_নাম = models.CharField(max_length=200) 
    date = models.DateTimeField(auto_now_add=True)