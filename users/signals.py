
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from .models import User


##### signal, which creates AuthN token once the user was registered
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=User, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)