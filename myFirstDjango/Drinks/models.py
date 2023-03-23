from django.db import models

# Create your models here.
class Drink(models.Model):
    uid = models.CharField(max_length=8)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=150)

    def __str__(self):
        return  self.name + ' ' + self.description
    