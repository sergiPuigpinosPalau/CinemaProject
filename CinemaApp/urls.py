from django.urls import path, include

from CinemaApp.views import MainPage

app_name = "CinemaApp"

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('', MainPage, name='home')
]