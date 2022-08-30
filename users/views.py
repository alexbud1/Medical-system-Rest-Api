from multiprocessing.connection import Client
from urllib import request
from rest_framework import viewsets, permissions, status, views, mixins
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db import transaction
from datetime import datetime
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
    AppointmentBelongsToOrganization,
    SessionResultBelongsToOrganization,
    ObjectBelongsToOrganization
)
from .utils import (
    serializer_create,
    check_week,
    Statistics,
    check_semester
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
    filter_backends = [ObjectBelongsToOrganization]
    permission_classes = () 

class ClientViewSet(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    ViewSet which retrieves, updates, destroys and creates Clients.
    """
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    filter_backends = [ObjectBelongsToOrganization]
    permission_classes = (IsAdminOrReadOnly,) 
 
class ListDoctorViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    ViewSet which returns a list of all doctors.
    """
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    filter_backends = [ObjectBelongsToOrganization]
    permission_classes = (IsAuthenticated,) 

class DoctorViewSet(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    ViewSet which retrieves, updates, destroys and creates Doctors.
    """
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    filter_backends = [ObjectBelongsToOrganization]
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
    filter_backends = [ObjectBelongsToOrganization]
    permission_classes = [IsAuthenticated]

class AdminViewSet(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    ViewSet which retrieves, updates, destroys and creates Admin.
    """
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer
    filter_backends = [ObjectBelongsToOrganization]
    permission_classes = [IsAdminOrReadOnly] 
 
class ListStaffViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    ViewSet which returns a list of all staff from organization.
    """
    queryset = OrganizationStaff.objects.all()
    serializer_class = OrganizationStaffSerializer
    filter_backends = [ObjectBelongsToOrganization]
    permission_classes = [IsAdminOrReadOnly]

class StaffViewSet(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    ViewSet which retrieves, updates, destroys and creates staff from organization.
    """
    queryset = OrganizationStaff.objects.all()
    serializer_class = OrganizationStaffSerializer
    filter_backends = [ObjectBelongsToOrganization]
    permission_classes = [IsAdminOrReadOnly] 

class ListDepartmentViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    ViewSet which returns a list of all staff from organization.
    """
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    filter_backends = [ObjectBelongsToOrganization]
    permission_classes = [IsAdminOrReadOnly]
 
class DepartmentViewSet(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    ViewSet which retrieves, updates, destroys and creates staff from organization.
    """
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    filter_backends = [ObjectBelongsToOrganization]
    permission_classes = [IsAdminOrReadOnly] 

def get_doctors_appointments(request):
    ##### check if the person, who send request is doctor
    doctor_quantity = Doctor.objects.filter(user=request.user).count()
    if doctor_quantity == 1:
        doctor = Doctor.objects.get(user=request.user)
        ##### list of all doctor's appointments
        appointments = Appointment.objects.filter(doctor=doctor.id)
        return appointments

class DoctorMonthlyStatisticsViewSet(viewsets.ViewSet):
    """
    ViewSet for retrieving doctor's monthly statistics.\n
    {\n
        "general amount of children" : 100,\n
        "amount of boys in age of 1-16" : 30,\n
        "amount of girls in age of 1-18" : 30,\n
        "amount of guys in age of 16-18" : 20,\n
        "amount of children in age of 0-1" : 15,\n
        "amount of disabled clients in age of 0-18" : 5\n
    }\n
    """  
    def list(self, request):
        appointments = get_doctors_appointments(request)
        if appointments:
            this_month = datetime.now().month
            this_year = datetime.now().year
            ##### appointments which were conducted this month only
            appointments = appointments.filter(start_time__month=this_month).filter(start_time__year=this_year)
            clients_id = []
            for appointment in appointments:
                if appointment.client.id not in clients_id:
                    ##### ids of clients for certain doctor
                    clients_id.append(appointment.client.id)
            ##### list of all clients filtered by month and doctor
            clients = Client.objects.filter(id__in = clients_id)

            stats_obj = Statistics(clients.count(), clients.boys16().count(), clients.girls().count(), clients.guys18().count(), clients.children().count(), clients.disabled().count())
            return Response(stats_obj.get_statistics())
        else:
            return Response(status = status.HTTP_400_BAD_REQUEST)




class DoctorWeeklyStatisticsViewSet(viewsets.ViewSet):
    def list(self, request):

        appointments = get_doctors_appointments(request)
        clients_id = []
        if appointments:
            for appointment in appointments:
                if check_week(appointment.start_time.strftime("%m/%d/%Y")):
                    if appointment.client.id not in clients_id:
                        ##### ids of clients for certain doctor
                        clients_id.append(appointment.client.id)
            ##### list of all clients filtered by week and doctor
            clients = Client.objects.filter(id__in = clients_id)

            stats_obj = Statistics(clients.count(), clients.boys16().count(), clients.girls().count(), clients.guys18().count(), clients.children().count(), clients.disabled().count())
            return Response(stats_obj.get_statistics())
        else:
            return Response(status = status.HTTP_400_BAD_REQUEST)

class DoctorSemesterStatisticsViewSet(viewsets.ViewSet):
    def list(self, request):

        appointments = get_doctors_appointments(request)
        clients_id = []
        if appointments:
            for appointment in appointments:
                if check_semester(appointment.start_time):
                    if appointment.client.id not in clients_id:
                        ##### ids of clients for certain doctor
                        clients_id.append(appointment.client.id)
            ##### list of all clients filtered by week and doctor
            clients = Client.objects.filter(id__in = clients_id)

            stats_obj = Statistics(clients.count(), clients.boys16().count(), clients.girls().count(), clients.guys18().count(), clients.children().count(), clients.disabled().count())
            return Response(stats_obj.get_statistics())
        else:
            return Response(status = status.HTTP_400_BAD_REQUEST)


class DoctorYearlyStatisticsViewSet(viewsets.ViewSet):
    def list(self, request):
        appointments = get_doctors_appointments(request)
        if appointments:
            this_year = datetime.now().year
            ##### appointments which were conducted this month only
            appointments = appointments.filter(start_time__year=this_year)
            clients_id = []
            for appointment in appointments:
                if appointment.client.id not in clients_id:
                    ##### ids of clients for certain doctor
                    clients_id.append(appointment.client.id)
            ##### list of all clients filtered by month and doctor
            clients = Client.objects.filter(id__in = clients_id)

            stats_obj = Statistics(clients.count(), clients.boys16().count(), clients.girls().count(), clients.guys18().count(), clients.children().count(), clients.disabled().count())
            return Response(stats_obj.get_statistics())
        else:
            return Response(status = status.HTTP_400_BAD_REQUEST)