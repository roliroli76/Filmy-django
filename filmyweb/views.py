from django.shortcuts import render
from django.http import HttpResponse
from .models import Film
# Create your views here.

def wszystkie_filmy(request):
    wszystkie = Film.objects.all()
    return render(request, 'filmy.html', {'filmy': wszystkie})

