from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Movie(models.Model):
    name = models.CharField(max_length=30)
    storyline = models.TextField()
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT)
    times_watched = models.IntegerField()

    def __str__(self):
        return self.name
