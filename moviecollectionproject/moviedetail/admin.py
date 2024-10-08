from django.contrib import admin
#from django.contrib import admin
from .models import Movie, MovieCollection

admin.site.register(Movie)
admin.site.register(MovieCollection)

# Register your models here.
