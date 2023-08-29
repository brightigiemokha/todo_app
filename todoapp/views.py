from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Todoitems

class TodoitemsList(ListView):
    model = Todoitems
    todo_object_name = 'tasks'

class TodoitemsDetail(DetailView):
    model = Todoitems
