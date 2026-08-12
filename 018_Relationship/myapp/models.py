from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20)
    
     
class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    price = models.FloatField()
    qty = models.IntegerField()
    image = models.ImageField(upload_to="image",default="test.png")


# class Enrollment(models.Model):
#     no = models.CharField(max_length=20)


# class Student(models.Model):
#     no = models.OneToOneField(Enrollment,on_delete=models.CASCADE)
#     name = models.CharField(max_length=50)
#     email = models.CharField(max_length=50)
#     age = models.IntegerField()
    
    
class Address(models.Model):
    country = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    
class Publisher(models.Model):
    address = models.ForeignKey(Address,on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    
class Author(models.Model):
    name = models.CharField(max_length=20)
    address = models.ForeignKey(Address,on_delete=models.CASCADE)
    
class Book(models.Model):
    publisher = models.ForeignKey(Publisher,on_delete=models.CASCADE)
    author = models.ManyToManyField(Author,related_name="book")
    name = models.CharField(max_length=20)
    price = models.FloatField()