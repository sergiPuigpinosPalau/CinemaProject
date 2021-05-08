from django import forms

from CinemaApp.models import Movie


class CreateFilmForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['name', 'description', 'genre', 'duration', 'released', 'poster']