from django.contrib import admin

from .models import (
    User, 
    Client,
    Doctor,
    Department,
    Organization,
    Appointment,
) 

for model in [User, Client, Doctor, Organization, Department, Appointment]:
    admin.site.register(model)
