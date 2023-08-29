from django.urls import path
from .views import TodoitemsList, TodoitemsDetail, TodoitemsCreate

urlpatterns = [
    path('', TodoitemsList.as_view(), name='todos'),
    path('todo/<int:pk>/', TodoitemsDetail.as_view(), name='todoitems'),
    path('todo-create/', TodoitemsCreate.as_view(), name='todo-create'),
]