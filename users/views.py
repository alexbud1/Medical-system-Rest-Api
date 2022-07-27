from multiprocessing.connection import Client
from django.shortcuts import render
from rest_framework import viewsets, permissions, status, views, mixins
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import (
    User,
    Client,
    Doctor
)

from .serializers import ( 
    UserSerializer,
    ClientSerializer,
    DoctorSerializer,
) 
 
class ClientUserViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    ViewSet which returns a list of all clients.
    """
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    filter_backends = []
    permission_classes = (IsAuthenticated,) 

class TestUrl(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        # email = request.user.email
        age = Client.objects.get(user=request.user.id)
        serializer = ClientSerializer(age, many=False)
        return Response(age.clients_age())

class DoctorUserViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    ViewSet which returns a list of all clients.
    """
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    filter_backends = []
    permission_classes = (IsAuthenticated,) 