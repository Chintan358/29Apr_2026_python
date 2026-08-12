from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=60)
    age = models.IntegerField()
    
class Product(models.Model):
    name = models.CharField(max_length=20)
    price = models.FloatField()
    qty = models.IntegerField()
    m_data = models.DateField()
    is_availble = models.BooleanField()
    