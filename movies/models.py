from django.db import models
class Movie(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    release_date = models.DateField()
    genre = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='movie_images/')
    def __str__(self):
        return self.name




