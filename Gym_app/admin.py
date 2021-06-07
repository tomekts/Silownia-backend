from django.contrib import admin
from .models import Exercises, Category, TrainingExercises, Training, Series
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class Exercisesadmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'categoryId','userId', 'public')
    list_filter = ('categoryId', 'name')



class Adminadmin(UserAdmin):
    list_display = ('id', 'username', 'email', 'is_active')


class Trainingadmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'date', 'userId')

class Seriesadmin(admin.ModelAdmin):
    list_display = ('id', 'TrainingExercisesId', 'TrainingId',  'weight', 'count')

class TrainingExercisesadmin(admin.ModelAdmin):
    list_display = ('id', 'trainingId', 'exercisesId', )

class Categoryadmin(admin.ModelAdmin):
    list_display = ('id', 'name')


admin.site.register(Category, Categoryadmin)
admin.site.register(Exercises, Exercisesadmin)

admin.site.register(Training, Trainingadmin)
admin.site.register(TrainingExercises, TrainingExercisesadmin)
admin.site.register(Series, Seriesadmin)
admin.site.register(get_user_model(), Adminadmin)