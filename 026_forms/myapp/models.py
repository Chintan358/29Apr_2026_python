from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=20)
    price = models.FloatField()
    qty = models.IntegerField()
