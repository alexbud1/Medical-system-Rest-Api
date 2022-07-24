import email
from django.db import models
from .managers import UserManager

class User(models.Model):
    email = models.EmailField(verbose_name = 'email address', max_length = 255, unique = True)
    objects = UserManager()
    def __str__ (self):
        return self.email
