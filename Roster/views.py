from django.shortcuts import render
from django.contrib.auth import get_user_model
from . import models
User = get_user_model()
# Create your views here.

def roster_home(request):
    context = { 'people': models.Person.objects.all()}
    return render(request, "roster_home.html", context)

