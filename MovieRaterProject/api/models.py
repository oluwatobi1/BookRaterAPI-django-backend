from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.


class Movie(models.Model):
    title = models.CharField(max_length=26)
    description = models.TextField(max_length=100)

    def __str__(self):
        return self.title


class Rating(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # Meaning if you'd delete a movie the user goes???
    stars = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)])

    class Meta:
        unique_together = (('user', 'movie'))
        indexes = [
            models.Index(fields=['user', 'movie']), ]
