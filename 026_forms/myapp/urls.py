from django.urls import path
from myapp.views import *


urlpatterns = [
    path("",index,name="index"),
    path("delete",delete_product,name="delete"),
    path("update",update_product,name="update")
]