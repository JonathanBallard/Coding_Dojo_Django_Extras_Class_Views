from django.db import models 
import re 
 
# create your models here 
# Field Types Link: https://docs.djangoproject.com/en/1.11/ref/models/fields/#field-types 




class Product(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()
    price = models.IntegerField()
    brand = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)











