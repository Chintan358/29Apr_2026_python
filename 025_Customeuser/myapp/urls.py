from django.urls import path
from myapp.views import *

urlpatterns = [
    path("register",register),
    path("student",student_api),
    path("faculty",faculty_api)
]