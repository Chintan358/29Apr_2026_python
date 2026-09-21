from rest_framework.serializers import ModelSerializer
from myapp.models import *
from rest_framework import exceptions
import re
from django.contrib.auth.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model=User
        fields='__all__'
        
        
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create_user(password=password,**validated_data)
        return user

class StudentSerializer(ModelSerializer):
    class Meta :
        model = Student
        fields='__all__'
        
    emailExp = r"^[0-9a-zA-Z._-]+@[a-zA-Z]+\.[a-zA-Z]{2,4}+$"
    def validate(self, attrs):
        if attrs['age']<18:
            raise exceptions.ValidationError({"age":"Age should be morethan 18 years"})
        
        if re.match(self.emailExp,attrs['email']) is None:
            raise exceptions.ValidationError({"Email":"Invalid email formate"})
        return super().validate(attrs)