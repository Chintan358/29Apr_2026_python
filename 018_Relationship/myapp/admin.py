from django.contrib import admin
from myapp.models import *
# Register your models here.

admin.site.register(Category)
admin.site.register(Product)

# admin.site.register(Enrollment)
# admin.site.register(Student)

admin.site.register(Address)
admin.site.register(Publisher)
admin.site.register(Author)
admin.site.register(Book)