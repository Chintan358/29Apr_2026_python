from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from myapp.models import *
from myapp.serializer import *
from rest_framework import status


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
        return Response({"erros":ser.errors,"message":"something went Wrong"},status=status.HTTP_400_BAD_REQUEST)
    else:
        ser.save()
        return Response({"data":ser.data,"message":"Student created"},status=status.HTTP_201_CREATED)
    
@api_view(['GET'])
def list_student(request):
    students = Student.objects.all()
    ser = Studentserializer(students,many=True)
    return Response({"data":ser.data},status=status.HTTP_200_OK)

@api_view(['GET'])
def retrive_student(request,id):
    try :
        student = Student.objects.get(id=id)
        ser = Studentserializer(student)
        return Response({"data":ser.data},status=status.HTTP_200_OK)
    except Student.DoesNotExist:
        return Response({"data":"Something went wrong"},status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['PUT'])
def update_student(request,id):
    try:
        stduent = Student.objects.get(id=id)
        ser= Studentserializer(stduent,request.data,partial=True)
        if not ser.is_valid():
            return Response({"erros":ser.errors,"message":"something went Wrong"},status=status.HTTP_400_BAD_REQUEST)
        else:
            ser.save()
            return Response({"data":ser.data,"message":"Student Updated"},status=status.HTTP_201_CREATED)
    except Student.DoesNotExist:
        return Response({"message":"Student not found"},status=status.HTTP_400_BAD_REQUEST)
  
@api_view(['DELETE'])  
def delete_student(request,id):
    try :
        student = Student.objects.get(id=id)
        student.delete()
        return Response({"data":"Student deleted"},status=status.HTTP_204_NO_CONTENT)
    except Student.DoesNotExist:
            return Response({"data":"Something went wrong"},status=status.HTTP_400_BAD_REQUEST)