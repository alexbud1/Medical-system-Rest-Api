from email.policy import default
from hashlib import blake2b
from django.db import models
from django.contrib.auth.models import AbstractUser
from .utils import *
import datetime
from phonenumber_field.modelfields import PhoneNumberField
from .querysets import  Boys16Queryset
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
    sex = models.CharField(max_length = 20, blank = True, choices = SEX_CHOICES)
    is_disabled = models.BooleanField(default=False)
    address = models.CharField(max_length = 300, blank = True, null=True)
    phone = PhoneNumberField(null=True, blank=True)
    client_of_org = models.ForeignKey(Organization, blank=False, on_delete=models.CASCADE)
    objects = Boys16Queryset.as_manager()
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
    appointment = models.OneToOneField(Appointment, on_delete=models.CASCADE, blank = False)
    diagnosis = models.CharField(max_length=400, blank = False, default="")
    complaints = models.CharField(max_length=400, blank = False)
    examination = models.CharField(max_length=400, blank = False)
    treatment = models.CharField(max_length=400, blank = False)
    payer = models.CharField(max_length=150, blank = False)
    price = models.IntegerField(blank = False)
    def __str__ (self):
        return f"{self.appointment.client} - {self.appointment.doctor}"

class Admin(models.Model):
    """ 
    this role is created for person, who can control all the processes
    in his/her organization
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank = False)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, blank = False)
    def __str__ (self):
        return f"Admin from {self.organization}"
 
class OrganizationStaff(models.Model):
    """
    administrator - this person is responsible for payments and can also create appointments for clients, who
    entered the clinic

    callcenter - this person has the same responsibilities as the administrator, but is not
    required to be present at the clinic
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank = False)
    role = models.CharField(max_length = 100, choices = STAFF_ROLE_CHOICES)
    first_name = models.CharField(max_length = 100, blank = False)
    last_name = models.CharField(max_length = 100, blank = False)
    fathers_name = models.CharField(max_length = 100, blank = True,null=True)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, blank = False)
    def __str__ (self):
        return self.last_name 
