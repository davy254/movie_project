from django.db import models

# Create your models here.
class Movie(models.Model):
    """
    Class for defining the Movie model
    """
    title = models.CharField(max_length=255)
    year = models.IntegerField()
    rating = models.FloatField()
    plot = models.TextField()

    def __str__(self):
        return self.title