from django.db import models

class Hotel(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    price = models.IntegerField()

class Menu(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=100)
    price = models.IntegerField()

# Create your models here.
