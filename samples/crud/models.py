from django.db import models


# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField(default=0)
    gender = models.CharField(max_length=32)
    department = models.CharField(max_length=32)
    designation = models.CharField(max_length=32)


    def __str__(self):
        return self.name
