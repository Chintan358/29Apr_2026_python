from rest_framework.permissions import BasePermission


class IsStudent(BasePermission):
    
     def has_permission(self, request, view):
          return request.user.role.name=='student' and request.user.is_authenticated
      


class IsFaculty(BasePermission):
    
    def has_permission(self, request, view):
           return request.user.role.name=='faculty' and request.user.is_authenticated