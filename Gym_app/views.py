from django.contrib.auth.views import LogoutView
from django.views import generic
# Create your views here.
from rest_framework import viewsets, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_jwt.views import JSONWebTokenAPIView

from rest_framework.response import Response
from datetime import datetime
from rest_framework import status
from rest_framework_jwt.settings import api_settings
from rest_framework_jwt.serializers import (
    JSONWebTokenSerializer, RefreshJSONWebTokenSerializer,
    VerifyJSONWebTokenSerializer
)


from .models import User, Exercises
from .serializers import UserSerializer, ExercisesSerializer

# testowe do django
class HomeView(generic.TemplateView):
    template_name = 'Gym_app/Home.html'

class Test(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request):
        res = Response()
        res.set_cookie(key="test", value="1234", httponly=True, samesite='None', secure=True)
        # res.delete_cookie('JW1', samesite='None', )
        res.data = {
            'Message': 'Logout complete'
        }
        return res

############## logowanie wylogowanie
class Logout(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request):
        res = Response()
        # res.set_cookie(key="test", value="123", httponly=True, samesite='None', secure=True)
        res.delete_cookie('JW1', samesite='None', )
        res.data = {
            'Message': 'Logout complete'
        }
        return res

class Login(JSONWebTokenAPIView):
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = JSONWebTokenSerializer
    def post(self, request, *args, **kwargs):
        serializer = JSONWebTokenAPIView.get_serializer(self, data=request.data)

        if serializer.is_valid():
            user = serializer.object.get('user') or request.user
            token = serializer.object.get('token')
            # response_data = api_settings.JWT_RESPONSE_PAYLOAD_HANDLER(token, user, request)
            # response_data =
            # response = Response(response_data)
            response = Response()
            response.data = {
                'Name': user.username.capitalize(),
                'Id': user.id,
            }
            if api_settings.JWT_AUTH_COOKIE:
                expiration = (datetime.utcnow() +
                              api_settings.JWT_EXPIRATION_DELTA)
                response.set_cookie(api_settings.JWT_AUTH_COOKIE,
                                    token,
                                    expires=expiration,
                                    httponly=True, secure=True, samesite='None' )

            return response

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#serializatory
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
class ExercisesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Exercises.objects.all()
    serializer_class = ExercisesSerializer
    # permission_classes = [permissions.IsAdminUser]