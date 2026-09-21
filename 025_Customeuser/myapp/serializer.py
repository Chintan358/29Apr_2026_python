from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from myapp.models import *

class RoleSerializer(ModelSerializer):
    class Meta:
        model = Role
        fields='__all__'

class UserSerilaizer(ModelSerializer):
    class Meta:
        model=CustomeUser
        fields='__all__'
        
    def create(self, validated_data):
        password = validated_data.pop("password")
        user = CustomeUser.objects.create_user(password=password,**validated_data)
        return user