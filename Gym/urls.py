"""Gym URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from Gym_app import views


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'exercises', views.ExercisesViewSet)
router.register(r'category', views.CategoryViewSet)
router.register(r'training', views.TrainingViewSet)
router.register(r'trainexer', views.TrainingExercisesViewSet)
router.register(r'series', views.SeriesViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Gym_app.urls')),
    path('rest/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]
