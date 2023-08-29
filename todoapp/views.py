from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Todoitems


class CustomLoginView(LoginView):
    template_name = 'todoapp/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('todoitemss')
        

class TodoitemsList(LoginRequiredMixin, ListView):
    model = Todoitems
    todo_object_name = 'todoitemss'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['todoitemss'] = context['todoitemss'].filter(user=self.request.user)
        context['count'] = context['todoitemss'].filter(complete=False).count()
        return context


class TodoitemsDetail(LoginRequiredMixin, DetailView):
    model = Todoitems
    context_object_name = 'todo'
    template_name = 'todoapp/todo_detail.html'


class TodoitemsCreate(LoginRequiredMixin, CreateView):
    model = Todoitems
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('todoitemss')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TodoitemsCreate, self).form_valid(form)


class TodoitemsUpdate(LoginRequiredMixin, UpdateView):
    model = Todoitems
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('todoitemss')


class DeleteView(LoginRequiredMixin, DeleteView):
    model = Todoitems
    context_object_name = 'todo'
    success_url = reverse_lazy('todoitemss')
