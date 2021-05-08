from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

from django.views.generic import CreateView, ListView, DetailView

from CinemaApp.forms import CreateFilmForm
from CinemaApp.models import *



class MainPage(ListView):
    model = Movie
    template_name = 'Home.html'
    context_object_name = 'movie_list'


class CreateMovie(CreateView):
    model = Movie
    template_name = 'CreateMovie.html'
    form_class = CreateFilmForm
    success_url = '/'


class DetailMovie(DetailView):
    model = Movie
    template_name = 'DetailMovie.html'
