from django.contrib.auth.decorators import login_required
from django.urls import path, include

from CinemaApp.views import *

app_name = "CinemaApp"

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('', login_required(MainPage.as_view()), name='home'),
    path('create_film', CreateMovie.as_view(), name='create_film'),
    path('delete_film/<int:pk>', DeleteMovie.as_view(), name='delete_film'),
    path('modify_film/<int:pk>', ModifyMovie.as_view(), name='modify_film'),
    path('detail_movie/<int:pk>', DetailMovie.as_view(), name='detail_movie'),
]