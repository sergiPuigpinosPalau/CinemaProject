import datetime

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.contrib.messages.views import SuccessMessageMixin
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


# Html

class MainPage(TemplateView):
    template_name = 'MainPage.html'

    def get_context_data(self, **kwargs):
        context = super(MainPage, self).get_context_data(**kwargs)
        context['latest_movies'] = Movie.objects.order_by('released')[:5]
        context['grup'] = check_group(self.request.user)
        return context


class MovieList(ListView):
    model = Movie
    template_name = 'Movies.html'
    context_object_name = 'movie_list'

    paginate_by = 6

    def get_queryset(self):
        try:
            return Movie.objects.all()
        except:
            return 0

    def get_context_data(self, **kwargs):
        context = super(MovieList, self).get_context_data(**kwargs)
        context['grup'] = check_group(self.request.user)
        return context


class CreateMovie(LoginRequiredMixin, CreateView):
    model = Movie
    template_name = 'CreateMovie.html'
    form_class = CreateFilmForm

    def get_context_data(self, **kwargs):
        context = super(CreateMovie, self).get_context_data(**kwargs)
        context['grup'] = check_group(self.request.user)
        return context


class DetailMovie(DetailView):
    model = Movie
    template_name = 'DetailMovie.html'

    def get_context_data(self, **kwargs):
        context = super(DetailMovie, self).get_context_data(**kwargs)
        context['grup'] = check_group(self.request.user)
        return context


class DeleteMovie(LoginRequiredMixin, DeleteView):
    model = Movie
    success_url = reverse_lazy('CinemaApp:movie_list')

    def get_context_data(self, **kwargs):
        context = super(DeleteMovie, self).get_context_data(**kwargs)
        context['grup'] = check_group(self.request.user)
        return context



class DeleteSession(LoginRequiredMixin, DeleteView):
    model = Session

    def get_success_url(self):
        return reverse('CinemaApp:detail_movie', kwargs={'pk': self.kwargs['pk_movie']})

    def get_context_data(self, **kwargs):
        context = super(DeleteSession, self).get_context_data(**kwargs)
        context['grup'] = check_group(self.request.user)
        return context



class ModifySession(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Session
    template_name = 'ModifySession.html'
    fields = ['hall', 'date', 'schedule']
    template_name_suffix = '_update_form'

    def form_valid(self, form):
        time = form.cleaned_data['schedule']
        form.instance.duration = datetime.datetime.strptime(time.end_time.isoformat(), '%H:%M:%S') - \
                                 datetime.datetime.strptime(time.starting_time.isoformat(), '%H:%M:%S')
        return super(ModifySession, self).form_valid(form)

    def get_success_url(self):
        return reverse('CinemaApp:detail_movie', kwargs={'pk': self.kwargs['pk_movie']})

    def get_success_message(self, cleaned_data):
        return "The session is modified "

    def get_context_data(self, **kwargs):
        context = super(ModifySession, self).get_context_data(**kwargs)
        context['grup'] = check_group(self.request.user)
        return context

class CreateSession(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Session
    form_class = CreateSessionForm
    template_name = 'CreateSession.html'

    def form_valid(self, form):
        form.instance.movie = Movie.objects.get(id=self.kwargs['pk'])
        time = form.cleaned_data['schedule']
        form.instance.duration = datetime.datetime.strptime(time.end_time.isoformat(), '%H:%M:%S') - \
                                 datetime.datetime.strptime(time.starting_time.isoformat(), '%H:%M:%S')
        return super(CreateSession, self).form_valid(form)

    def get_success_url(self):
        return reverse('CinemaApp:detail_movie', kwargs={'pk': self.kwargs['pk']})

    def get_success_message(self, cleaned_data):
        return "The session was created "

    def get_context_data(self, **kwargs):
        context = super(CreateSession, self).get_context_data(**kwargs)
        context['grup'] = check_group(self.request.user)
        return context

def check_group(user):
    try:
        group =  Group.objects.get(name='trabajador')
        return group in user.groups.all()
    except Group.DoesNotExist:
        return False