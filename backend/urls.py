from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static

urlpatterns = [
    path("api/users/", include("users.urls"), name="users"),
    path("admin/", admin.site.urls),
] 