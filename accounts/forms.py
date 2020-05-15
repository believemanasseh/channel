from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser


class CustomUserForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ['email', 'username', 'password1', 'password2']