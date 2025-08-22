from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    #path('', views.roster_home, name="roster-default" ),
    #path('', views.PersonView.as_view(), name="person-list" ),
    path('', views.roster_home.as_view(), name="roster-home" ),
    path('people', views.roster_home.as_view(), name="roster-home" ),
    path('people/list', views.load_people, name="roster-load-people"),
    path('people/create/', views.CreatePerson.as_view(), name="person-create" ),
    path('people/<slug:slug>/', views.UpdatePerson.as_view(), name='person-edit'),
    path('people/delete/<slug:slug>/', views.DeletePerson.as_view(), name='person-delete'),
]