from datetime import timedelta

from django.conf import settings
from django.utils import timezone
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import AuthenticationFailed


def is_token_expired(token):
    expired = token.created + timedelta(seconds=settings.TOKEN_EXPIRED_AFTER_SECONDS) < timezone.now()
    return expired

 
class ExpiringTokenAuthentication(TokenAuthentication):
    """
    The same authentication mechanism as default token authentication in DRF, but
    with simple expiration premise. Expiration time can be adjusted in settings.py.
    This custom authentication class is specified in settings.py as default.
    """
    def authenticate_credentials(self, key):
        try:
            token = Token.objects.get(key=key)
        except Token.DoesNotExist:
            raise AuthenticationFailed("Invalid token")

        if not token.user.is_active:
            raise AuthenticationFailed("User inactive or deleted")

        expired = is_token_expired(token)
        if expired:
            token.delete()
            Token.objects.create(user=token.user)
            raise AuthenticationFailed("Token has expired")

        return (token.user, token)