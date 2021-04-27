from django.urls import path
from Gym_app.views import *
from . import views
from django.conf.urls.static import static
from rest_framework_jwt.views import obtain_jwt_token
from django.conf import settings

app_name = 'Gym'
urlpatterns = [
    path('', views.HomeView.as_view(), name='Home'),
    path('login/', views.Login.as_view(), name='Login'),
    path('logout/', views.LogoutView.as_view(), name='Logout'),
    path('test/', views.Test.as_view(), name='test'),
    path('log/', views.Log.as_view(), name='log'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
