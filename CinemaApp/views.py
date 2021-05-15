from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator

from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView, TemplateView

from CinemaApp.forms import CreateFilmForm, CreateSessionForm
from CinemaApp.models import *


class LoginRequiredMixin(object):
    @method_decorator(login_required())
    def dispatch(self, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(*args, **kwargs)


#Html

class MainPage(TemplateView):
    template_name = 'MainPage.html'

    def get_context_data(self, **kwargs):
        context = super(MainPage, self).get_context_data(**kwargs)
        context['latest_movies'] = Movie.objects.order_by('released')[:5]
        return context


class MovieList(ListView):
    model = Movie
    template_name = 'Movies.html'
    context_object_name = 'movie_list'


class CreateMovie(LoginRequiredMixin, CreateView):
    model = Movie
    template_name = 'CreateMovie.html'
    form_class = CreateFilmForm
    #success_url = reverse_lazy('CinemaApp:movie_list')


class DetailMovie(DetailView):
    model = Movie
    template_name = 'DetailMovie.html'


class DeleteMovie(LoginRequiredMixin, DeleteView):
    model = Movie
    success_url = reverse_lazy('CinemaApp:movie_list')


class ModifyMovie(LoginRequiredMixin, UpdateView):
    model = Movie
    success_url = reverse_lazy('CinemaApp:movie_list')


class CreateSession(LoginRequiredMixin, CreateView):
    model = Session
    form_class = CreateSessionForm
    template_name = 'CreateSession.html'

    def form_valid(self, form):
        form.instance.movie = Movie.objects.get(id=self.kwargs['pk'])
        return super(CreateSession, self).form_valid(form)

    def get_success_url(self):
        return reverse('CinemaApp:detail_movie', kwargs={'pk': self.kwargs['pk']})