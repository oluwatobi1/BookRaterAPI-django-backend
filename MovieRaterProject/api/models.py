from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.


class Movie(models.Model):
    title = models.CharField(max_length=26)
    description = models.TextField(max_length=100)

    def no_of_rating(self):
        rating = Rating.objects.filter(movie = self)
        return len(rating)

    def avg_rating(self):
        rating = Rating.objects.filter(movie=self)
        sum=0
        for each in rating:
            sum+=each.stars

        if len(rating)!=0:
            return sum/len(rating)
        else:
            return 0


    def __str__(self):
        return self.title


class Rating(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # Meaning if you'd delete a movie the user goes???
    stars = models.IntegerField(
                          validators=[MinValueValidator(0),
                                      MaxValueValidator(5)])

    class Meta:
        unique_together = (('user', 'movie'))
        indexes = [
            models.Index(fields=['user', 'movie']), ]
