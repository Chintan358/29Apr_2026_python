from django.urls import path
from myapp.views import *

urlpatterns = [
        path("create",create_student),
        path("register",register_user)
]