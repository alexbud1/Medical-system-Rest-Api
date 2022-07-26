from django.urls import path
from rest_framework.routers import SimpleRouter
from . import views
from rest_framework.authtoken.views import obtain_auth_token

router = SimpleRouter()
router.register(r"users", views.ListUserViewSet, basename="roles")
appname = "users" 
urlpatterns = router.urls + [
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('test_url/', views.TestUrl.as_view(), name='test_url'),

]