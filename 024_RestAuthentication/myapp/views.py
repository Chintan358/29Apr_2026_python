from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view,APIView,permission_classes
from myapp.models import *
from myapp.serializer import *
from rest_framework.permissions import IsAdminUser,IsAuthenticated,AllowAny

@api_view(['POST'])
@permission_classes([IsAdminUser])
def create_student(request):
    ser = StudentSerializer(data = request.data)
    if ser.is_valid():
        ser.save()
        return Response({"data":ser.data})
    else:
        return Response({"errors":ser.errors})
    

   
@api_view(['POST']) 
def register_user(request):
    ser = UserSerializer(data = request.data)
    if ser.is_valid():
        ser.save()
        return Response({"data":ser.data})
    else:
        return Response({"errors":ser.errors})
        