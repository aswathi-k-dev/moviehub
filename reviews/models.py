
from django.db import models
from django.contrib.auth.models import User
from films.models import Movie

# Create your models here.

class Review(models.Model):

    movie = models.ForeignKey(Movie,on_delete=models.CASCADE,related_name='reviews')

    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='reviews')

    message = models.TextField()

    rating = models.FloatField()

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('movie', 'user')

    def __str__(self):
        return f"{self.movie.title} - {self.user.username} - {self.rating}"