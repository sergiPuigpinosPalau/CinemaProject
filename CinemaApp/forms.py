from django import forms

from CinemaApp.models import *


class CreateFilmForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['name', 'description', 'genre', 'duration', 'released', 'poster']


class CreateSessionForm(forms.ModelForm):
    class Meta:
        model = Session
        fields = ['hall', 'schedule']