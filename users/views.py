from multiprocessing.connection import Client
from pydoc import Doc
from django.shortcuts import render
from rest_framework import viewsets, permissions, status, views, mixins
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import (
    User, 
    Client,
    Doctor,
    Department,
    Organization,
    Appointment,
    SessionResult,
    Admin,
    OrganizationStaff,
) 

from .serializers import ( 
    UserSerializer,
    ClientSerializer,
    DoctorSerializer,
    AppointmentSerializer,
    DepartmentSerializer,
    OrganizationSerializer,
    SessionResultSerializer,
    AdminSerializer,
    OrganizationStaffSerializer

) 
from .permissions import (
    YourClientOrReadOnly,
    IsSuperUserOrReadOnly,
)
from .filters import (
    ClientBelongsToOrganization,
    DoctorBelongsToOrganization,
    AppointmentBelongsToOrganization,
    SessionResultBelongsToOrganization
)

class TestUrl(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        # email = request.user.email
        # age = Client.objects.get(user=request.user.id)
        # serializer = ClientSerializer(age, many=False)

        return Response(age.clients_age())


class ListClientViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    ViewSet which returns a list of all clients.
    """
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    filter_backends = [ClientBelongsToOrganization]
    permission_classes = (IsAuthenticated,) 

class ClientViewSet(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    ViewSet which retrieves, updates, destroys and creates Clients.
    """
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    filter_backends = [ClientBelongsToOrganization]
    permission_classes = (IsSuperUserOrReadOnly,) 
 
class ListDoctorViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    ViewSet which returns a list of all doctors.
    """
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    filter_backends = [DoctorBelongsToOrganization]
    permission_classes = (IsAuthenticated,) 

class DoctorViewSet(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    ViewSet which retrieves, updates, destroys and creates Doctors.
    """
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    filter_backends = [DoctorBelongsToOrganization]
    permission_classes = [IsSuperUserOrReadOnly]

class ListAppointmentViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    ViewSet which returns a list of all appointments.
    """
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    filter_backends = [AppointmentBelongsToOrganization]
    permission_classes = [IsAuthenticated]
 
class AppointmentViewSet(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    ViewSet which retrieves, updates, destroys and creates Appointment.
    """
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    filter_backends = [AppointmentBelongsToOrganization]
    permission_classes = [YourClientOrReadOnly]

class ListSessionResultViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    ViewSet which returns a list of all appointments.
    """
    queryset = SessionResult.objects.all()
    serializer_class = SessionResultSerializer
    filter_backends = [SessionResultBelongsToOrganization]
    permission_classes = [IsAuthenticated]