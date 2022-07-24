from django.urls import path
from rest_framework.routers import SimpleRouter
from . import views

router = SimpleRouter()
router.register(r"users", views.ListUserViewSet, basename="roles")
appname = "users"

urlpatterns = router.urls