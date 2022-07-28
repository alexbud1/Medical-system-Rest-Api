from rest_framework import filters
from .models import *

class ClientBelongsToOrganization(filters.BaseFilterBackend):
    """
    Filter that only allows doctors to see clients only from their organization.
    """
    def filter_queryset(self, request, queryset, view):
        doctor = Doctor.objects.get(user=request.user)
        return queryset.filter(client_of_org=doctor.organization)

class DoctorBelongsToOrganization(filters.BaseFilterBackend):
    """
    Filter that only allows doctors to see other doctors only from their organization.
    """
    def filter_queryset(self, request, queryset, view):
        doctor = Doctor.objects.get(user=request.user)
        return queryset.filter(organization=doctor.organization)

class AppointmentBelongsToOrganization(filters.BaseFilterBackend):
    """
    Filter that only allows doctors to see other doctors only from their organization.
    """
    def filter_queryset(self, request, queryset, view):
        doctor = Doctor.objects.get(user=request.user)
        doctors = Doctor.objects.filter(organization=doctor.organization)
        return queryset.filter(doctor__in=doctors)