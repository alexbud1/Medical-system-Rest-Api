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

appname = "users" 
urlpatterns = router.urls + [
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('test_url/', views.TestUrl.as_view(), name='test_url'),

]