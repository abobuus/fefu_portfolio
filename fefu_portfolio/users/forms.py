from django.contrib.auth import admin, get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import forms


class RegisterForm(UserCreationForm):
    ...
