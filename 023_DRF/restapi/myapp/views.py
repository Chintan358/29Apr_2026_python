from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from myapp.models import *
from myapp.serializer import *


@api_view(['POST'])
def create_api(request):
    return Response("POST api calling")


@api_view(['GET'])
def list_api(request):
    return Response("GET api calling")


@api_view(['PUT'])
def update_api(request):
    return Response("PUT api calling")


@api_view(['DELETE'])
def delete_api(request):
    return Response("DELETE api calling")



@api_view(['POST'])
def create_student(request):
    data = request.data
    ser =  Studentserializer(data = data)
    if not ser.is_valid():
        return Response({"erros":ser.errors,"message":"something went Wrong"})
    else:
        ser.save()
        return Response({"data":ser.data,"message":"Student created"})
    
@api_view(['GET'])
def list_student(request):
    students = Student.objects.all()
    ser = Studentserializer(students,many=True)
    return Response({"data":ser.data})