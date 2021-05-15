from django.contrib.auth.decorators import login_required
from django.urls import path, include

from CinemaApp.views import *

app_name = "CinemaApp"

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('', MainPage.as_view(), name='home'),
    path('movies', MovieList.as_view(), name='movie_list'),
    path('movies/create_movie', CreateMovie.as_view(), name='create_movie'),
    path('movies/<int:pk>/delete', DeleteMovie.as_view(), name='delete_movie'),
    path('movies/<int:pk>/edit', ModifyMovie.as_view(), name='modify_movie'),
    path('movies/<int:pk>', DetailMovie.as_view(), name='detail_movie'),
    path('movies/<int:pk>/session/create', CreateSession.as_view(), name='create_session'),
]