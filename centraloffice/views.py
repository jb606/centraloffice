from django.shortcuts import render

def co_home_view(request):
    return render(request, "cohome.html", {} )