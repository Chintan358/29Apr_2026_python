from django.urls import path
from myapp.views import *

urlpatterns = [    
    path("create",create_api,name="create"),
    path("list",list_api, name="list"),
    path("update",update_api,name="update"),
    path("delete",delete_api,name="delete"),
    
    
    path("create-student",create_student,name="create-student"),
    path("list-student",list_student,name="list-student"),
    path("retrive-student/<id>",retrive_student,name="retrive-student"),
    path("update-student/<id>",update_student,name="update-student"),
    path("delete-student/<id>",delete_student,name="delete-student")
    
]