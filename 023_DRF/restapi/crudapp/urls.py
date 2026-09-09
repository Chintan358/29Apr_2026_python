from django.urls import path
from crudapp.views import *

urlpatterns = [
    
    path("all",EmployeeApi.as_view()),
    path("all/<id>",EmployeeById.as_view())
]