
from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path("", views.co_home_view, name="home"),
    path("admin/", admin.site.urls),
    path("accounts/", include('allauth.urls')),
    path("people", include('Roster.urls')),

]
