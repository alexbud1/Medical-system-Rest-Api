from django.contrib import admin

from .models import (
    User, 
    Client,
    Doctor,
    Department,
    Organization,
) 

for model in [User, Client, Doctor, Organization, Department]:
    admin.site.register(model)
