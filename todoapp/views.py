from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Todoitems
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class TodoitemsList(ListView):
    model = Todoitems
    todo_object_name = 'todos'


class TodoitemsDetail(DetailView):
    model = Todoitems
    context_object_name = 'todo'
    template_name = 'todoapp/todo_detail.html'


class TodoitemsCreate(CreateView):
    model = Todoitems
    fields = '__all__'
    success_url = reverse_lazy('todos')


class TodoitemsUpdate(UpdateView):
    model = Todoitems
    fields = '__all__'
    success_url = reverse_lazy('todos')


class DeleteView(DeleteView):
    model = Todoitems
    context_object_name = 'todo'
    success_url = reverse_lazy('todos')
