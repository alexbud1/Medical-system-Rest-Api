from audioop import add
import email
from re import T
from django.db import models
# from .managers import UserManager
from django.contrib.auth.models import AbstractUser
from .utils import *
import datetime
from phonenumber_field.modelfields import PhoneNumberField
 
class User(AbstractUser):
    email = models.EmailField(verbose_name = 'email address', max_length = 255, unique = True)
    def __str__ (self):
        return self.email 

class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank = False)
    first_name = models.CharField(max_length = 100, blank = False)
    last_name = models.CharField(max_length = 100, blank = False)
    fathers_name = models.CharField(max_length = 100, blank = True,null=True)
    birthday = models.DateField(blank=False)
    address = models.CharField(max_length = 300, blank = True, null=True)
    phone = PhoneNumberField(null=True, blank=True, unique=True)
    def __str__ (self):
        return self.last_name 

    def clients_age(self):
        return int((datetime.date.today() - self.birthday).days / 365.25  )

def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank = False)
    first_name = models.CharField(max_length = 100, blank = False)
    last_name = models.CharField(max_length = 100, blank = False)
    fathers_name = models.CharField(max_length = 100, blank = True,null=True)
    specialization = models.CharField(max_length = 200, blank = False)
    education = models.CharField(max_length = 300, blank = False)
    photo = models.ImageField(upload_to=upload_to, blank=True, null=True)
    def __str__ (self):
        return self.last_name 

class Department(models.Model):
    address = models.CharField(max_length = 300, blank = False)
    def __str__ (self):
        return self.address 

class Organization(models.Model):
    name = models.CharField(max_length = 100, blank = False)
    doctors = models.ManyToManyField(Doctor, blank = True)
    departments = models.ManyToManyField(Department, blank = True)
    def __str__ (self):
        return self.name 