from django.contrib.auth.decorators import login_required
from django.urls import path, include

from CinemaApp.views import MainPage

app_name = "CinemaApp"

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('', login_required(MainPage), name='home')
]