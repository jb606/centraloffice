
from django.contrib import admin
from django.urls import path, include

#import Roster.views
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.co_home_view, name="home"),
    path('accounts/', include('allauth.urls')),
    path("roster/", include('Roster.urls')),
]


