from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def test_response(request):
    return HttpResponse("<h1>To jest mój pierwszy test</h1>")
