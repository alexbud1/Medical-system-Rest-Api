from hashlib import blake2b
from django.db import models
from django.contrib.auth.models import AbstractUser
from .utils import *
from datetime import datetime
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
    email = models.EmailField(verbose_name = 'email address', max_length = 255)
    """unique = True  was not used because the same person 
    can be registered in different organizations and in fact the User object will be different(with 
    mobile phone there is the same situation) """
    def __str__ (self):
        return self.email 

def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)


class Organization(models.Model):
    name = models.CharField(max_length = 100, blank = False)
    def __str__ (self):
        return self.name 

class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank = False)
    first_name = models.CharField(max_length = 100, blank = False)
    last_name = models.CharField(max_length = 100, blank = False)
    fathers_name = models.CharField(max_length = 100, blank = True,null=True)
    birthday = models.DateField(blank=False)
    address = models.CharField(max_length = 300, blank = True, null=True)
    phone = PhoneNumberField(null=True, blank=True)
    client_of_org = models.ForeignKey(Organization, blank=False, on_delete=models.CASCADE)
    def __str__ (self):
        return self.last_name 
    
    def clients_age(self):
        return int((datetime.date.today() - self.birthday).days / 365.25  )
        
class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank = False)
    first_name = models.CharField(max_length = 100, blank = False)
    last_name = models.CharField(max_length = 100, blank = False)
    fathers_name = models.CharField(max_length = 100, blank = True,null=True)
    specialization = models.CharField(max_length = 100, choices = SPECIALIZATION_CHOICES)
    education = models.CharField(max_length = 300, blank = False)
    photo = models.ImageField(upload_to=upload_to, blank=True, null=True)
    organization = models.ForeignKey(Organization, blank = False, on_delete=models.CASCADE)
    def __str__ (self):
        return self.last_name 

class Department(models.Model):
    address = models.CharField(max_length = 300, blank = False)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, blank = False)
    def __str__ (self):
        return self.address 

class Appointment(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, blank = False)
    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE, blank = False)
    start_time = models.DateTimeField(blank=False)
    end_time = models.DateTimeField(blank=False)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, blank = False)
    def __str__ (self):
        data = self.start_time.strftime("%m/%d/%Y, %H:%M:%S")
        return f"{self.client.last_name} {data}"

class SessionResult(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE, blank = False)
    diagnosis = models.CharField(max_length=400, blank = False)
    def __str__ (self):
        return f"{self.appointment.client} - {self.appointment.doctor}"