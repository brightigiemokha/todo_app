from django.urls import path
from .views import TodoitemsList, TodoitemsDetail, TodoitemsCreate, TodoitemsUpdate, DeleteView, CustomLoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),

    path('', TodoitemsList.as_view(), name='todoitemss'),
    path('todo/<int:pk>/', TodoitemsDetail.as_view(), name='todo'),
    path('todo-create/', TodoitemsCreate.as_view(), name='todo-create'),
    path('todo-update/<int:pk>/', TodoitemsUpdate.as_view(), name='todo-update'),
    path('todo-delete/<int:pk>/', DeleteView.as_view(), name='todo-delete'),
]