from django.urls import path

from .views import index, authors

urlpatterns = [
    path('', index),
    path('authors/', authors)
]
