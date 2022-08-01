from math import perm
from rest_framework import permissions
from .models import *

##### Doctor can edit only his/her appointments
class YourClientOrReadOnly(permissions.BasePermission):
    edit_methods = ("PUT", "PATCH")

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True
 
        ##### check if appointment is specified for this doctor
        doctor = Doctor.objects.get(user=request.user)
        if doctor.id == obj.doctor.id:
            return True

        if request.method not in self.edit_methods:
            return True

        return False
 
##### only superuser is allowed to edit or delete users and doctors
class IsSuperUserOrReadOnly(permissions.BasePermission):
    edit_methods = ("PUT", "PATCH")

    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.is_superuser:
            return True

        if request.method not in self.edit_methods:
            return True
        return False

##### only superuser, admin from this organization and doctor, who conducted the examination can access
##### session result
class YourSessionResultOrReadOnly(permissions.BasePermission):
    edit_methods = ("PUT", "PATCH")
 
    def has_object_permission(self, request, view, obj):
        # if request.user.is_superuser:
        #     return True
 
        ##### check if session result was created by this doctor
        doctor = Doctor.objects.get(user=request.user)
        print(obj.appointment.doctor)
        # if doctor.id == obj.doctor.id:
        #     return True

        # if request.method not in self.edit_methods:
        #     return True

        return False

class IsAdminOrReadOnly(permissions.BasePermission):
    edit_methods = ("PUT", "PATCH")

    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True

        admin_quantity = Admin.objects.filter(user=request.user).count()
        if admin_quantity == 1:
            return True

        if request.method not in self.edit_methods:
            return True
        return False