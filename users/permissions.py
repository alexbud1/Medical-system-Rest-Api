from rest_framework import permissions
from .models import *
class YourClientOrReadOnly(permissions.BasePermission):
    edit_methods = ("PUT", "PATCH")

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True

        if Doctor.objects.get(user = request.user).id == obj.doctor:
            return True

        if request.method not in self.edit_methods:
            return True

        return False