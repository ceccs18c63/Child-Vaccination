from django.db import models

# Create your models here.

class Child(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    def __str__(self):
        return self.name

class Hospitals(models.Model):
    id1 = models.IntegerField()
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    def __str__(self):
        return self.name

