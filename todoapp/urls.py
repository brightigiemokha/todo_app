from django.urls import path
from .views import TodoitemsList, TodoitemsDetail, TodoitemsCreate, TodoitemsUpdate, DeleteView

urlpatterns = [
    path('', TodoitemsList.as_view(), name='todos'),
    path('todo/<int:pk>/', TodoitemsDetail.as_view(), name='todo'),
    path('todo-create/', TodoitemsCreate.as_view(), name='todo-create'),
    path('todo-update/<int:pk>/', TodoitemsUpdate.as_view(), name='todo-update'),
    path('todo-delete/<int:pk>/', DeleteView.as_view(), name='todo-delete'),
]