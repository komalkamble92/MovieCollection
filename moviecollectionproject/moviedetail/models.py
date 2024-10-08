from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255)
    genre = models.CharField(max_length=100)
    release_date = models.DateField()

    def __str__(self):
        return f"{self.title} ({self.release_date.year}) - Genre: {self.genre}"
# Create your models here.
class MovieCollection(models.Model):
    name = models.CharField(max_length=255)
    movies = models.ManyToManyField(Movie, related_name='collections')

    def __str__(self):
        return self.name
