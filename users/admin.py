from django.contrib import admin

from .models import (
    User, 
    Client,
) 

for model in [User, Client]:
    admin.site.register(model)
