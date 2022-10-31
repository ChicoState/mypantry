from dataclasses import fields
from unicodedata import category
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class ingredient(models.Model):
    name =  models.CharField(max_length=255)
    quantity = models.CharField(max_length=20)
    unit =  models.CharField(max_length=50)
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    
class recipe(models.Model):
    title = models.CharField(max_length=255)
    directions = models.TextField()
    content = models.TextField()
    ingredients = models.ForeignKey(ingredient,on_delete=models.CASCADE, null=True)
    category = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class UserModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username

