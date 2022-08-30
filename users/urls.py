from django.urls import path
from rest_framework.routers import SimpleRouter
from . import views
from rest_framework.authtoken.views import obtain_auth_token

router = SimpleRouter()
router.register(r"clients", views.ListClientViewSet, basename="clients")
router.register(r"client", views.ClientViewSet, basename="client")
router.register(r"doctors", views.ListDoctorViewSet, basename="doctors")
router.register(r"doctor", views.DoctorViewSet, basename="doctor")
router.register(r"appointments", views.ListAppointmentViewSet, basename="appointments")
router.register(r"appointment", views.AppointmentViewSet, basename="appointment")
router.register(r"sessionresults", views.ListSessionResultViewSet, basename="sessionresults")
router.register(r"sessionresult", views.SessionResultViewSet, basename="sessionresult")
router.register(r"admins", views.ListAdminViewSet, basename="admins")
router.register(r"admin", views.AdminViewSet, basename="admin")
router.register(r"all_staff", views.ListStaffViewSet, basename="all_staff")
router.register(r"staff", views.StaffViewSet, basename="staff")
router.register(r"departments", views.ListDepartmentViewSet, basename="departments")
router.register(r"department", views.DepartmentViewSet, basename="department")
router.register(r"signup", views.SignUpViewSet, basename="user_signup")
router.register(r"doctor_monthly_stats", views.DoctorMonthlyStatisticsViewSet, basename="doctor_stats")
router.register(r"doctor_weekly_stats", views.DoctorWeeklyStatisticsViewSet, basename="doctor_stats")
appname = "users" 
urlpatterns = router.urls + [
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('test_url/', views.TestUrl.as_view(), name='test_url'),

] 