from django.db import models

# Create your models here.
class Actors(models.Model):
    first_name      = models.CharField(max_length=25)
    last_name       = models.CharField(max_length=25)
    date_of_birth   = models.DateField()

    class Meta:
        db_table    = 'actor'

class Movies(models.Model):
    title           = models.CharField(max_length=25)
    release_date    = models.DateField()
    running_time    = models.IntegerField()
    actor           = models.ManyToManyField('Actor',related_name='movie')

    class Meta:
        db_table = 'movie'