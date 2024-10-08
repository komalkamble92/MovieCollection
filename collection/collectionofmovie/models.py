from django.db import models

# Create your models here.
from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    release_date = models.DateField()
    genre = models.CharField(max_length=50)
    description = models.TextField()
    def __str__(self):
        return self.title