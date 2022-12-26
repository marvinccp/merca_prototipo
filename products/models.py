from django.db import models
from django.core.exceptions import ValidationError


class Category(models.Model):

    name = models.CharField(max_length=200, null=False, blank=False)
    code = models.IntegerField(unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50, null=False)
    quantity = models.IntegerField(default=10)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    code = models.IntegerField(unique=True)
    notes = models.CharField(max_length=300, default='Sin novedad')
    format = models.CharField(max_length=50, default= '1Kg')


    def __str__(self):
        return self.name
