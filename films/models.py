from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Movie(models.Model):

    LANGUAGE_CHOICES = [
        ('Malayalam', 'Malayalam'),
        ('English', 'English'),
        ('Tamil', 'Tamil'),
        ('Hindi', 'Hindi'),
        ('Kannada','Kannada')
    ]

    GENRE_CHOICES = [
        ('ACTION', 'Action'),
        ('COMEDY', 'Comedy'),
        ('DRAMA', 'Drama'),
        ('THRILLER', 'Thriller'),
        ('ROMANCE', 'Romance'),
    ]

    title = models.CharField(max_length=200)

    language = models.CharField(max_length=200,choices=LANGUAGE_CHOICES)

    genre = models.CharField(max_length=200,choices=GENRE_CHOICES)

    actor = models.CharField(max_length=100)

    release_year = models.PositiveIntegerField()

    rating = models.FloatField(default=0)

    created_by = models.ForeignKey(User,on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

