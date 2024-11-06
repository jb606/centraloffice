from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.roster_home, name="roster-default" ),
    path('people/', views.PersonView.as_view(), name="person-list" ),
    path('people/create/', views.CreatePerson.as_view(), name="person-create" ),
    path('people/<int:pk>/', views.UpdateTemplate.as_view(), name='person-edit'),
    path('people/delete/<int:pk>/', views.DeletePerson.as_view(), name='person-delete'),
]