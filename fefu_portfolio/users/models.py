from django.db import models


class Users(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    patronymic = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    is_verifier = models.BooleanField(default=False)
