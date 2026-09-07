from rest_framework import serializers
from myapp.models import *


class Studentserializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields='__all__'