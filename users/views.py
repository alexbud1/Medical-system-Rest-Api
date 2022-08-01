from multiprocessing.connection import Client
from pydoc import Doc
from django.shortcuts import render
from rest_framework import viewsets, permissions, status, views, mixins
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from django.db import transaction
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
    OrganizationStaffSerializer,
    CreateUserSerializer,

) 
from .permissions import (
    YourClientOrReadOnly,
    IsSuperUserOrReadOnly,
    YourSessionResultOrReadOnly,
    IsAdminOrReadOnly,
)
from .filters import (
    ClientBelongsToOrganization,
    DoctorBelongsToOrganization,
    AppointmentBelongsToOrganization,
    SessionResultBelongsToOrganization,
    AdminBelongsToOrganization,
)
from .utils import (
    serializer_create,
    
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
    permission_classes = (IsAdminOrReadOnly,) 
 
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
    permission_classes = [IsAdminOrReadOnly]

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
    permission_classes = [YourClientOrReadOnly,IsAdminOrReadOnly]
 
class ListSessionResultViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    ViewSet which returns a list of all session results.
    """
    queryset = SessionResult.objects.all()
    serializer_class = SessionResultSerializer
    filter_backends = [SessionResultBelongsToOrganization]
    permission_classes = [IsAuthenticated]

class SessionResultViewSet(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    ViewSet which retrieves, updates, destroys and creates Session Result.
    """
    queryset = SessionResult.objects.all()
    serializer_class = SessionResultSerializer
    filter_backends = [SessionResultBelongsToOrganization]
    permission_classes = [YourSessionResultOrReadOnly, IsAdminOrReadOnly]

class SignUpViewSet(viewsets.ViewSet):
    """
    ViewSet which is responsible for a sign up process using credentials
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    @transaction.atomic
    def create(self, request):
        """
        Sign-up route by email,username and password. 
        If data isn't acceptable, all changes to the database will be reversed.
        """
        user_data = {
            'email' : request.data.pop('email'),
            'username': request.data.pop('username'),
            'password': request.data.pop('password')
        }
        savepoint = transaction.savepoint()
        try:
            user = serializer_create(CreateUserSerializer, data = user_data)
            request.data["user"] = user["id"]
        except Exception as e:
            transaction.savepoint_rollback(savepoint)
            return Response(str(e),  status = status.HTTP_400_BAD_REQUEST)
        return Response(data = user,  status = status.HTTP_201_CREATED)

class ListAdminViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    ViewSet which returns a list of all admins.
    """
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer
    filter_backends = [AdminBelongsToOrganization]
    permission_classes = [IsAuthenticated]

class AdminViewSet(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    ViewSet which retrieves, updates, destroys and creates Admin.
    """
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer
    filter_backends = [AdminBelongsToOrganization]
    permission_classes = [IsAdminOrReadOnly] 

class ListStaffViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    ViewSet which returns a list of all staff from organization.
    """
    queryset = OrganizationStaff.objects.all()
    serializer_class = OrganizationStaffSerializer
    filter_backends = [AdminBelongsToOrganization]
    permission_classes = [IsAdminOrReadOnly]

class StaffViewSet(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    ViewSet which retrieves, updates, destroys and creates staff from organization.
    """
    queryset = OrganizationStaff.objects.all()
    serializer_class = OrganizationStaffSerializer
    filter_backends = [AdminBelongsToOrganization]
    permission_classes = [IsAdminOrReadOnly] 

class ListDepartmentViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    ViewSet which returns a list of all staff from organization.
    """
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    filter_backends = [AdminBelongsToOrganization]
    permission_classes = [IsAdminOrReadOnly]

class DepartmentViewSet(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    ViewSet which retrieves, updates, destroys and creates staff from organization.
    """
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    filter_backends = [AdminBelongsToOrganization]
    permission_classes = [IsAdminOrReadOnly] 