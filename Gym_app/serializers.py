from rest_framework import serializers
from .models import Exercises, User, Category,Training,TrainingExercises,Series
from django.contrib.auth import get_user_model # If used custom user model


class RegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=50, min_length=6)
    username = serializers.CharField(max_length=50, min_length=5)
    password = serializers.CharField(max_length=100, write_only=True, min_length=6)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


    def validate(self, args):
        email = args.get('email', None)
        username = args.get('username', None)
        User.is_active = False
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError({'username': ('Juz występuje')})
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'email': ('Juz występuje')})
        return super().validate(args)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'groups', 'password', 'last_name']
        extra_kwargs = {'password': {'write_only': True}}


class ExercisesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercises
        fields = ['id','name']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class TrainingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Training
        fields = '__all__'

class TrainingExercisesSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainingExercises
        fields = '__all__'


class SeriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Series
        fields = '__all__'
