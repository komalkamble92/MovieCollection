from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Movie
from .serializers import MovieSerializer
from django.http import Http404



from rest_framework import viewsets
from .models import Movie
from .serializers import MovieSerializer

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
