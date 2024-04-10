from django.urls import path
from . import views

# Author: Jason Ngo, Maxine Ramos, Jenny Shen, Joyce Xuan
# Class: INF 453 - Capstone Project
# Supervisor: Maher Elshakankiri
# Purpose: URLS for redirecting users (mainly to go back to main page)

app_name = 'dashboard'

urlpatterns = [
    path('', views.index, name='index'),
]