from django.db import models
from django.core import validators as v
from django.core.validators import *

# Create your models here.
class Brands(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return f"Brand_name: {self.name}"

class Models(models.Model):
    model_name = models.CharField(max_length=250)
    brands = models.ForeignKey(Brands, on_delete=models.CASCADE, related_name='brand')

    def __str__(self):
        return f"Model_name: {self.model_name}"
