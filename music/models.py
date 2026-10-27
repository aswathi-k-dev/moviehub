from django.db import models
from django.contrib.auth.models import User
from films.models import Movie

# Create your models here.

class Song(models.Model):

    LANGUAGE_CHOICES = [
        ('Malayalam', 'Malayalam'),
        ('English', 'English'),
        ('Tamil', 'Tamil'),
        ('Hindi', 'Hindi'),
    ]

    GENRE_CHOICES = [
        ('MELODY', 'Melody'),
        ('ROMANTIC', 'Romantic'),
        ('DEVOTIONAL', 'Devotional'),
        ('FOLK', 'Folk'),
        ('POP', 'Pop'),
    ]

    title = models.CharField(max_length=200)

    language = models.CharField(max_length=200,choices=LANGUAGE_CHOICES)

    genre = models.CharField(max_length=200,choices=GENRE_CHOICES)

    singer = models.CharField(max_length=100)

    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    duration = models.FloatField()

    track_number = models.IntegerField()

    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
            
            last_song_object = Song.objects.filter(movie=self.movie).last()

            if last_song_object:
                self.track_number = last_song_object.track_number + 1
            else:
                self.track_number = 1

            return super().save(*args, **kwargs)

    def __str__(self):
        return self