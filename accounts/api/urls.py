from django.urls import include, path
from .views import RegisterView


urlpatterns = [
    path("", include("rest_auth.urls")),
    path("register/", include("rest_auth.registration.urls")),
]
