from dj_rest_auth.views import LoginView
from dj_rest_auth.registration.views import RegisterView
from .serializers import RegisterSerializer

class LoginView(LoginView):
    pass

class RegisterView(RegisterView):
    serializer_class = RegisterSerializer
