from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import (
    User, 
    Client,
    Doctor,
    Department,
    Organization,
    Appointment,
    SessionResult,
    Admin,
    OrganizationStaff,
) 

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'
 
class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = '__all__'


class DoctorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Doctor
        fields = '__all__'

class AppointmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Appointment
        fields = '__all__'

class DepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Department
        fields = '__all__'

class OrganizationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Organization
        fields = '__all__'

class SessionResultSerializer(serializers.ModelSerializer):

    class Meta:
        model = SessionResult
        fields = '__all__'

class AdminSerializer(serializers.ModelSerializer):

    class Meta:
        model = Admin
        fields = '__all__'

class OrganizationStaffSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrganizationStaff
        fields = '__all__'

class CreateUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=68, min_length=6, write_only=True)

    def validate_password(self, value: str) -> str:
        return make_password(value)

    class Meta:
        model = User
        fields = ["id", "email","username", "password"] 