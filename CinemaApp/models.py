from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Genre(models.Model):
    GENRE_TYPES = (('act', 'Action'), ('adv', 'Adventure'), ('ani', 'Animated'), ('com', 'Comedy'), ('dra', 'Drama'),
                   ('fan', 'Fantasy'), ('his', 'Historical'), ('hor', 'Horror'), ('sci', 'Science fiction'),
                   ('thr', 'Thriller'), ('wes', 'Western'))
    name_genre = models.CharField(max_length=4, choices=GENRE_TYPES)

    def __str__(self):
        return self.name_genre


class Movie(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    duration = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name


class Hall(models.Model):
    capacity = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return "Hall: " + str(self.id)


class Schedule(models.Model):
    starting_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return "Schedule: " + str(self.id)


class Reservation(models.Model):
    price = models.FloatField()
    buy_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return "Reservation: " + str(self.id)


class Session(models.Model):
    duration = models.IntegerField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)    #TODO limit to 1
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.date)
