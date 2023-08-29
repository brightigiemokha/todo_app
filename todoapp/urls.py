from django.urls import path
from .views import TodoitemsList, TodoitemsDetail

urlpatterns = [
    path('', TodoitemsList.as_view(), name='todoitems'),
    path('todo_items/<int:pk>/', TodoitemsDetail.as_view(), name='todo_items'),
]