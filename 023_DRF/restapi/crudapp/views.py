from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view,APIView
from crudapp.models import *
from crudapp.serializer import *
from rest_framework import status

class EmployeeApi(APIView):

    def post(self,request):
        try :
            ser = EmployeeSerializer(data=request.data)
            if not ser.is_valid():
                return Response({"errors":ser.errors,"message":"something went wrong"},status=status.HTTP_400_BAD_REQUEST)
            else:
                ser.save()
                return Response({"data":ser.data,"message":"Employee created"},status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"message":e})
    
    def get(self,request):
        try :
           emps = Employee.objects.all()
           ser = EmployeeSerializer(emps,many=True)
           return Response({"data":ser.data})
        except Exception as e:
                    return Response({"message":e})
        

class EmployeeById(APIView):
    
    def get(self,request,id):
        try :
            emps = Employee.objects.get(id=id)
            ser = EmployeeSerializer(emps)
            return Response({"data":ser.data})
        except Employee.DoesNotExist as e:
            return Response({"message":"Employee not found"})
        
    def put(self,request,id):
        try :
            emps = Employee.objects.get(id=id)
            ser = EmployeeSerializer(emps,request.data)
            if not ser.is_valid():
                return Response({"errors":ser.errors,"message":"something went wrong"},status=status.HTTP_400_BAD_REQUEST)
            else:
                ser.save()
                return Response({"data":ser.data,"message":"Employee updated"},status=status.HTTP_201_CREATED)
        except Exception as e:
                    return Response({"message":e})
    
    def delete(self,request,id):
        try :
            emps = Employee.objects.get(id=id)
            emps.delete()
            return Response({"message":"emp deleted"})
        except Employee.DoesNotExist as e:
                    return Response({"message":"Employee not found"})