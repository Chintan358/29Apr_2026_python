from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view,APIView,permission_classes
from myapp.models import *
from myapp.serializer import *
from myapp.permissions import *

@api_view(['POST'])
def register(request):
    ser = UserSerilaizer(data=request.data)
    if ser.is_valid():
        ser.save()
        return Response({"data":ser.data})
    else:
        return Response({"error":ser.errors})
    
@api_view(['GET'])
@permission_classes([IsStudent])
def student_api(request):
    return Response("Student api calling")

@api_view(['GET'])
@permission_classes([IsFaculty])
def faculty_api(request):
    return Response("faculty api calling")