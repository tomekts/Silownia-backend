from django.urls import path
from Gym_app.views import *
from . import views


app_name = 'Gym'
urlpatterns = [
    path('', views.HomeView.as_view(), name='Home'),

]