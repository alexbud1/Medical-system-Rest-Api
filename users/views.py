from django.shortcuts import render
from rest_framework import viewsets, permissions, status, views, mixins
from rest_framework.generics import GenericAPIView

from .models import (
    User,
)

from .serializers import ( 
    UserSerializer,
)
 
class ListUserViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    ViewSet which returns a list of notifications.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = []
    permission_classes = [permissions.AllowAny]