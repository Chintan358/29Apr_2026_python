from django.db import models
from django.contrib.auth.models import AbstractBaseUser,AbstractUser
from django.contrib.auth.models import User
from myapp.manager import *




class Role(models.Model):
    name = models.CharField(max_length=20)

# Create your models here.
class CustomeUser(AbstractUser):
        role = models.ForeignKey(Role,on_delete=models.CASCADE,null=True)
        phone = models.CharField(max_length=20,unique=True,default="test" )      
        USERNAME_FIELD = "phone"   
        objects=UserManager()