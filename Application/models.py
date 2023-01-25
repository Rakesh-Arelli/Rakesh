from django.db import models


# Create your models here.
class PatientModel(models.Model):
    name=models.CharField(max_length=20,null=True)
    age=models.IntegerField(null=True)
    gen = [
        ('m', 'Male'),
        ('f', 'Female'),
        ('o', 'Other')
    ]
    Gender= models.CharField(max_length=3, choices=gen,null=True)
    startCity=models.CharField(max_length=50,null=True)
    Destination = models.CharField(max_length=20,null=True)
    price=models.IntegerField(null=True)