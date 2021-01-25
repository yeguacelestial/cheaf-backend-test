from django.urls import path, include
from rest_framework import routers

from random_words import views


urlpatterns = [
    path('', views.RandomWords.as_view()),
]