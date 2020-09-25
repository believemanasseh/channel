from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
#from django.contrib.auth.models import User

from .models import CustomUser
from .forms import CustomUserForm


class CustomUserAdmin(UserAdmin):
    form = CustomUserForm
    model = CustomUser
    list_display = ['email', 'username']


admin.site.register(CustomUser, CustomUserAdmin)
