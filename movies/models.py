from django.db import models

# Create your models here.
class Actors(models.Model):
    first_name      = models.CharField(max_length=25)
    last_name       = models.CharField(max_length=25)
    date_of_birth   = models.DateField()

    class Meta:
        db_table = 'owner'

class Dog(models.Model):
    name     = models.CharField(max_length=25)
    age      = models.IntegerField(default=0)
    owner    = models.ForeignKey('Owner', on_delete=models.CASCADE)

    class Meta:
        db_table = 'dog'