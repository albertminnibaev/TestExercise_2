from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model

from users.validators import EmailValidators, PasswordValidators

User = get_user_model()


class UserRegistrationSerializer(BaseUserRegistrationSerializer):

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'date_of_birth', 'password', 'image']
        validators = [
            EmailValidators(fields=('email',)),
            PasswordValidators(fields=('password',))
        ]


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'date_of_birth', 'password', 'image']


class CurrentUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'date_of_birth', 'password', 'image']
