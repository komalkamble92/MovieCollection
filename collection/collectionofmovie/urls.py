#from django.urls import path
#from .views import * # . = root path
from .api import * # all classes imported

#from . import api
#from collectionofmovie import views 
#from django.urls import path
#from .views import movie_list, movie_detail, movie_add
from rest_framework.routers import DefaultRouter
from django.urls import path, include
#from rest_framework.routers import DefaultRouter
from .views import *



urlpatterns = [
    path('movie/', movie_list, name='movie_list'),
    path('movie/<int:movie_id>/', movie_detail, name='movie_detail'),
    path('movie/add/', movie_add, name='movie_add'),

    # path('movielist/',movie_list.as_view(),name='movielist'),
    # path('moviedetail/',movie_detail.as_view(),name='moviedetail'),
    # path('movieadd/',movie_add.as_view(),name='movieadd')
    #router == DefaultRouter(),
    #router.register(r'movies', MovieViewSet),

    #path('', include('.urls')),





]


