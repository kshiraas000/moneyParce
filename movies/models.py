from django.db import models

# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=255)
    release_date = models.DateField()
    genre = models.CharField(max_length=100)

    def __str__(self):
        return self.name