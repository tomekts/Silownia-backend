from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import ugettext_lazy as _
import os
from datetime import date
# Create your models here.


class User(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)


class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Kategoria'
        verbose_name_plural = 'Kategorie'


class Exercises(models.Model):
    def urla(self, filename):
        return os.path.join('images/exercises/', filename)

    name = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to=urla, blank=True)
    categoryId = models.ForeignKey('Category', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Cwiczenie'
        verbose_name_plural = 'Cwiczenia'

class Training(models.Model):
    name = models.CharField(max_length=200, blank=True)
    userId = models.ForeignKey('User', on_delete=models.CASCADE)
    date = models.DateField(default=date.today)
    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name = 'Trening'
        verbose_name_plural = 'Treningi'


class TrainingExercises(models.Model):
    trainingId = models.ForeignKey('Training', on_delete=models.CASCADE, verbose_name='id treningu')
    exercisesId = models.ForeignKey('Exercises', on_delete=models.CASCADE, verbose_name='cwiczenie')

    def __str__(self):
        return str(self.pk)




    class Meta:
        verbose_name = 'Cwiczenia treningu'
        verbose_name_plural = 'Cwiczenia treningu'

class Series(models.Model):
    TrainingExercisesId = models.ForeignKey('TrainingExercises', on_delete=models.CASCADE, verbose_name='id cwiczenia treningu')
    weight = models.IntegerField()
    count = models.IntegerField()
    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name = 'Seria'
        verbose_name_plural = 'Serie'