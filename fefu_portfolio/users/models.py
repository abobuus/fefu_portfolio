from django.contrib.auth import get_user_model
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin, AbstractUser
from django.db import models


class User(AbstractUser):
    DoesNotExist = None
    pass

    def __str__(self):
        return self.username


