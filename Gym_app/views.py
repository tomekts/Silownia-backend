from django.contrib.auth.views import LogoutView
from django.views import generic
# Create your views here.


class HomeView(generic.TemplateView):
    template_name = 'Gym_app/Home.html'


class Login(generic.TemplateView):
    template_name = 'Gym_app/Login.html'


class LogoutView(LogoutView):
    template_name = 'Gym_app/Home.html'
