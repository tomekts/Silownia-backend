from django.contrib.auth.views import LogoutView
from django.views import generic
# Create your views here.
from rest_framework import viewsets

from .models import User, Exercises
from .serializers import UserSerializer, ExercisesSerializer


class HomeView(generic.TemplateView):
    template_name = 'Gym_app/Home.html'


class Login(generic.TemplateView):
    template_name = 'Gym_app/Login.html'


class LogoutView(LogoutView):
    template_name = 'Gym_app/Home.html'


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    # permission_classes = [permissions.IsAdminUser]


class ExercisesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Exercises.objects.all()
    serializer_class = ExercisesSerializer
    # permission_classes = [permissions.IsAdminUser]