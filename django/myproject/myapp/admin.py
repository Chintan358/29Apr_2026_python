from django.contrib import admin
from myapp.models import *

# Register your models here.
class StudentView(admin.ModelAdmin):
    list_display=['id','name','email','age']
    
class ProductView(admin.ModelAdmin):
    list_display=['id','name','price','qty','m_data','is_availble']

admin.site.register(Student,StudentView)
admin.site.register(Product,ProductView)