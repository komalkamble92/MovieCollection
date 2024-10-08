from django.urls import path
from .views import * # . = root path
from collectionofmovie.api import * # all classes imported

from . import api
from collectionofmovie import views 
from django.urls import path
from .views import movie_list, movie_detail, movie_add

urlpatterns = [
    path('movie/', movie_list, name='movie_list'),
    path('movie/<int:movie_id>/', movie_detail, name='movie_detail'),
    path('movie/add/', movie_add, name='movie_add'),
]


