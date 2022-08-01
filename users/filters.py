from subprocess import call
from rest_framework import filters
from .models import *
from rest_framework.response import Response
from rest_framework import status


class ClientBelongsToOrganization(filters.BaseFilterBackend):
    """
    Filter that only allows employees to see clients only from their organization.
    """
    def filter_queryset(self, request, queryset, view):
        doctor_quantity = Doctor.objects.filter(user=request.user).count()
        if doctor_quantity == 1:
            doctor = Doctor.objects.get(user=request.user)
            return queryset.filter(client_of_org=doctor.organization)
        else:
            if request.user.is_superuser:
                return queryset
            else:
                admin_quantity = Admin.objects.filter(user=request.user).count()
                if admin_quantity == 1:
                    admin = Admin.objects.get(user=request.user)
                    return queryset.filter(client_of_org=admin.organization)
                else:
                    staff_quantity = OrganizationStaff.objects.filter(user=request.user).count()
                    if staff_quantity == 1:
                        staff = OrganizationStaff.objects.get(user=request.user)
                        return queryset.filter(client_of_org=staff.organization)

class DoctorBelongsToOrganization(filters.BaseFilterBackend):
    """
    Filter that only allows employees to see other doctors only from their organization.
    """
    def filter_queryset(self, request, queryset, view):
        doctor_quantity = Doctor.objects.filter(user=request.user).count()
        if doctor_quantity == 1:
            doctor = Doctor.objects.get(user=request.user)
            return queryset.filter(organization=doctor.organization)
        else:
            if request.user.is_superuser:
                return queryset
            else:
                admin_quantity = Admin.objects.filter(user=request.user).count()
                if admin_quantity == 1:
                    admin = Admin.objects.get(user=request.user)
                    return queryset.filter(organization=admin.organization)
                else:
                    staff_quantity = OrganizationStaff.objects.filter(user=request.user).count()
                    if staff_quantity == 1:
                        staff = OrganizationStaff.objects.get(user=request.user)
                        return queryset.filter(organization=staff.organization)
 
class AppointmentBelongsToOrganization(filters.BaseFilterBackend):
    """
    Filter that only allows employees to see other appointments only from their organization.
    """
    def filter_queryset(self, request, queryset, view):
        doctor_quantity = Doctor.objects.filter(user=request.user).count()
        if doctor_quantity == 1:
            doctor = Doctor.objects.get(user=request.user)
            doctors = Doctor.objects.filter(organization=doctor.organization)
            return queryset.filter(doctor__in=doctors)
        else:
            if request.user.is_superuser:
                return queryset
            else:
                admin_quantity = Admin.objects.filter(user=request.user).count()
                if admin_quantity == 1:
                    admin = Admin.objects.get(user=request.user)
                    doctors = Doctor.objects.filter(organization=admin.organization)
                    return queryset.filter(doctor__in=doctors)
                else:
                    staff_quantity = OrganizationStaff.objects.filter(user=request.user).count()
                    if staff_quantity == 1:
                        staff = OrganizationStaff.objects.get(user=request.user)
                        doctors = Doctor.objects.filter(organization=staff.organization)
                        return queryset.filter(doctor__in=doctors)

class SessionResultBelongsToOrganization(filters.BaseFilterBackend):
    """
    Filter that only allows employees to see Session Result only from their organization.
    """
    def filter_queryset(self, request, queryset, view):
        doctor_quantity = Doctor.objects.filter(user=request.user).count()
        if doctor_quantity == 1:
            doctor = Doctor.objects.get(user=request.user)
            doctors = Doctor.objects.filter(organization=doctor.organization)
            appointments = Appointment.objects.filter(doctor__in=doctors)
            return queryset.filter(appointment__in=appointments)
        else:
            if request.user.is_superuser:
                return queryset
            else:
                admin_quantity = Admin.objects.filter(user=request.user).count()
                if admin_quantity == 1:
                    admin = Admin.objects.get(user=request.user)
                    doctors = Doctor.objects.filter(organization=admin.organization)
                    appointments = Appointment.objects.filter(doctor__in=doctors)
                    return queryset.filter(appointment__in=appointments)
                else:
                    staff_quantity = OrganizationStaff.objects.filter(user=request.user).count()
                    if staff_quantity == 1:
                        staff = OrganizationStaff.objects.get(user=request.user)
                        doctors = Doctor.objects.filter(organization=staff.organization)
                        appointments = Appointment.objects.filter(doctor__in=doctors)
                        return queryset.filter(appointment__in=appointments)

class AdminBelongsToOrganization(filters.BaseFilterBackend):
    """
    Filter that only allows employees to see admins only from their organization.
    """
    def filter_queryset(self, request, queryset, view):
        doctor_quantity = Doctor.objects.filter(user=request.user).count()
        if doctor_quantity == 1:
            doctor = Doctor.objects.get(user=request.user)
            return queryset.filter(organization=doctor.organization)
        else:
            if request.user.is_superuser:
                return queryset
            else:
                admin_quantity = Admin.objects.filter(user=request.user).count()
                if admin_quantity == 1:
                    admin = Admin.objects.get(user=request.user)
                    return queryset.filter(organization=admin.organization)
                else:
                    staff_quantity = OrganizationStaff.objects.filter(user=request.user).count()
                    if staff_quantity == 1:
                        staff = OrganizationStaff.objects.get(user=request.user)
                        return queryset.filter(organization=staff.organization)

# class AdminBelongsToOrganization(filters.BaseFilterBackend):
#     """
#     Filter that only allows employees to see staff only from their organization.
#     """
#     def filter_queryset(self, request, queryset, view):
#         doctor_quantity = Doctor.objects.filter(user=request.user).count()
#         if doctor_quantity == 1:
#             doctor = Doctor.objects.get(user=request.user)
#             return queryset.filter(organization=doctor.organization)
#         else:
#             if request.user.is_superuser:
#                 return queryset
#             else:
#                 admin_quantity = Admin.objects.filter(user=request.user).count()
#                 if admin_quantity == 1:
#                     admin = Admin.objects.get(user=request.user)
#                     return queryset.filter(organization=admin.organization)
#                 else:
#                     staff_quantity = OrganizationStaff.objects.filter(user=request.user).count()
#                     if staff_quantity == 1:
#                         staff = OrganizationStaff.objects.get(user=request.user)
#                         return queryset.filter(organization=staff.organization)