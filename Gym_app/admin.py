from django.contrib import admin
from .models import Exercises
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
# Register your models here.


admin.site.register(Exercises)
admin.site.register(get_user_model(), UserAdmin)