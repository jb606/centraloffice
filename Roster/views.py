from django.shortcuts import render, HttpResponse
from django.contrib import messages
from .models import Person
from .forms import AffilationForm

# Create your views here.

def home(request):
    p = Person.objects.all()
    page_context = { 'people': p, }
    return render(request, "people_home.html", {'people' :p} )

