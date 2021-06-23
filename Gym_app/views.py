from django.contrib.auth.views import LogoutView
from django.views import generic
from datetime import datetime
# Create your views here.
import json
from .utils import send_email
# from django.core.mail import send_mail
from rest_framework import viewsets, permissions, status, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_jwt.views import JSONWebTokenAPIView

from rest_framework.response import Response
from rest_framework_jwt.settings import api_settings
from rest_framework_jwt.serializers import JSONWebTokenSerializer


from .utils import generate_token, send_email
from django.utils.encoding import force_bytes, force_text


from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.template.loader import render_to_string
from .forms import UserTestForm
from django.contrib.sites.shortcuts import get_current_site
from .models import User, Exercises, Category, Training, TrainingExercises, Series
from .serializers import RegistrationSerializer
from .serializers import UserSerializer, ExercisesSerializer, CategorySerializer, TrainingSerializer, TrainingExercisesSerializer, SeriesSerializer

import environ
env = environ.Env(DEBUG=(bool, False))

# testowe do django


class HomeView(generic.TemplateView):
    template_name = 'Gym_app/Home.html'


class Test(APIView):
    # permission_classes = [permissions.IsAuthenticated]
    def post(self, request):
        res = Response()
        # res.set_cookie(key="test", value="1234", httponly=True, samesite='None', secure=True)
        # res.delete_cookie('JW1', samesite='None', )
        res.data = {
            'Message': 'Logout complete'
        }


        return Response(status=201)







############## logowanie wylogowanie rejestracja Test_zalogowania
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


class RegisterViewSet(APIView):
    # permission_classes = [permissions.AllowAny]

    def post(self, request):
        request_data = json.load(request)
        form = UserTestForm(request_data)



        if form.is_valid():
            form.save()
            adress = form.data['email']
            user = User.objects.get(email=adress)
            file = render_to_string('Gym_app/email_message/activate_email.html', {
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': generate_token.make_token(user),
                'domain': env('URL'),
                'user': user
            })
            send_email("Witaj " + user.username.capitalize(), adress, file)
            return Response(form.errors, status=201)
        return Response(form.errors)


class Activ(APIView):

    def post(self, request):
        date = json.load(request)
        token = date['token']
        uidb64 = date['uid']
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except Exception as identifier:
            user = None
        if user is not None and generate_token.check_token(user, token):
            user.is_active = True
            user.save()
            res = Response()
            res.data = {
                'Message': 'Aktywacja konta'
            }
            return res

        return Response(status=405)

class Check(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request):
        res = Response()
        res.data = {
            'Message': 'Logined'
        }
        return Response(status=200)

#serializatory
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ExercisesViewSet(viewsets.ModelViewSet):

    queryset = Exercises.objects.all()
    serializer_class = ExercisesSerializer
    filterset_fields = ('categoryId', 'name', 'public', 'userId')  # here
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CategoryViewSet(viewsets.ModelViewSet):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # permission_classes = [permissions.IsAdminUser]


class TrainingViewSet(viewsets.ModelViewSet):
    queryset = Training.objects.all().order_by('-id')
    serializer_class = TrainingSerializer
    filterset_fields = ('id',  'userId')  # here
    # permission_classes = [permissions.IsAdminUser]


class TrainingExercisesViewSet(viewsets.ModelViewSet):
    queryset = TrainingExercises.objects.all()
    serializer_class = TrainingExercisesSerializer
    filterset_fields = ('id', 'trainingId')  # here
    # permission_classes = [permissions.IsAdminUser]


class SeriesViewSet(viewsets.ModelViewSet):
    queryset = Series.objects.all()
    serializer_class = SeriesSerializer
    filterset_fields = ('id', 'TrainingExercisesId', 'TrainingId')  # here
    permission_classes = [permissions.IsAuthenticated]