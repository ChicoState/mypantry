from dataclasses import fields
from unicodedata import category
from django.db import models
from django.contrib.auth.models import User

class Recipe(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    directions = models.CharField(max_length=65536)
    category = models.CharField(max_length=255)

class Ingredient(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    name =  models.CharField(max_length=255)
    quantity = models.CharField(max_length=20)
    unit =  models.CharField(max_length=50)
    recipe = models.ForeignKey(Recipe, blank=True, null=True, on_delete=models.CASCADE)

class Grocery(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name =  models.CharField(max_length=255)
    quantity = models.CharField(max_length=20)
    unit =  models.CharField(max_length=50)

class JournalEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    datetime = models.DateField(auto_now=True)
    description = models.CharField(max_length=128)
    entry = models.CharField(max_length=65536)