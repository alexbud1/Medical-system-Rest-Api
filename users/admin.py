from django.contrib import admin

from .models import (
    User, 
)

for model in [User]:
    admin.site.register(model)
