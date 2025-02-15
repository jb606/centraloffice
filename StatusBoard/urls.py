from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('group/', views.GroupListView.as_view(), name="sb-default" ),
    path('group/<int:pk>/', views.GroupView.as_view(), name="sb-group-view" ),
    path('group/add/', views.GroupCreate.as_view(), name='sb-group-create')
]