from django.urls import path
from .views import TodoitemsList

urlpatterns = [
    path('', TodoitemsList.as_view(), name='todoitems')
]