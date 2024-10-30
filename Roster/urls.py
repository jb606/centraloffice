from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.roster_home, name='roster_home')
]