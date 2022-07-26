from django.shortcuts import render
from rest_framework import viewsets, permissions, status, views, mixins
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import (
    User,
)

from .serializers import ( 
    UserSerializer,
) 
 
class ListUserViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    ViewSet which returns a list of all users.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = []
    permission_classes = (IsAuthenticated,) 

class TestUrl(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        email = request.user.email
        return Response(email)