from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import ugettext_lazy as _
# Create your models here.


class User(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)


class Exercises(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name
