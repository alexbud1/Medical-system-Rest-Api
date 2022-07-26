import email
from django.db import models
# from .managers import UserManager
from django.contrib.auth.models import AbstractUser
from .utils import *
import datetime

 
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
    def __str__ (self):
        return self.last_name

    def clients_age(self):
        return int((datetime.date.today() - self.birthday).days / 365.25  )