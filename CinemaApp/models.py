from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.urls import reverse


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Movie(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    genre = models.CharField(max_length=100, null=True, blank=True)
    duration = models.CharField(max_length=100, null=True, blank=True)
    released = models.CharField(max_length=100, null=True, blank=True)
    poster = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('CinemaApp:detail_movie', kwargs={'pk': self.pk})


class Hall(models.Model):
    capacity = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return "Hall: " + str(self.id)


class Schedule(models.Model):
    starting_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return "Schedule from " + str(self.starting_date) + " to " + str(self.end_date)

#TODO eliminar?
class Reservation(models.Model):
    price = models.FloatField()
    buy_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return "Reservation: " + str(self.id)


class Session(models.Model):
    duration = models.IntegerField(null=True, blank=True) #TODO eliminar
    date = models.DateField(null=True, blank=True)  #TODO eliminar
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movie_sessions')
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)    #TODO limit to 1
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.date)
