from django.contrib import admin

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

for model in [User, Client, Doctor, Organization, Department, Appointment, SessionResult, Admin, OrganizationStaff]:
    admin.site.register(model)
