from rest_framework import serializers

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
        exclude = ['client_of_org']

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