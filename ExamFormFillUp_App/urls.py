from argparse import Namespace
from django import views
from django.urls import path
from .views import showformdata
urlpatterns = [
    path('', showformdata),
]
