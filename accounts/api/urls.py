from django.urls import include, path
from .views import RegisterView


urlpatterns = [
    path("", include("dj_rest_auth.urls")),
    path("register/", include("dj_rest_auth.registration.urls")),
]
