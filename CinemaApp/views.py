from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

#class MainPage(DetailView):

def MainPage(r):
    return HttpResponse("Hola")
