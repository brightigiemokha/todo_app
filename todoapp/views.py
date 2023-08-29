from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Todoitems

class TodoitemsList(ListView):
    model = Todoitems
