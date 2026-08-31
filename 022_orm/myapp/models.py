from django.db import models

class Dept(models.Model):
    name= models.CharField(max_length=20)

class Student(models.Model):
    dept = models.ForeignKey(Dept,on_delete=models.CASCADE,related_name="students")
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    age = models.IntegerField()
    
