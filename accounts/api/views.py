from rest_auth.views import LoginView
from rest_auth.registration.views import RegisterView
from .serializers import RegisterSerializer

class LoginView(LoginView):
    pass

class RegisterView(RegisterView):
    serializer_class = RegisterSerializer
