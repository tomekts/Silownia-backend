from rest_framework import serializers
from .models import Exercises, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'groups', 'password', 'last_name']
        extra_kwargs = {'password': {'write_only': True}}


class ExercisesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercises
        fields = ['id','name']