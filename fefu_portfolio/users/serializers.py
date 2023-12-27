from abc import ABC

from rest_framework import serializers, exceptions
from django.contrib.auth.hashers import check_password
from .models import User


class UserInfoSerializers(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    _response = None

    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']

        try:
            user = User.objects.get(username=username)
            if not (check_password(password, user.password)):
                raise exceptions.ValidationError("Неверный пароль")

        except User.DoesNotExist:
            raise exceptions.ValidationError("Неверные данные авторизации")

        self._response = {
            "username": username,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email,
            "is_staff": user.is_staff
        }
        return user

    def get_response(self):
        return self._response
