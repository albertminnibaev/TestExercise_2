from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model

from users.validators import EmailValidators, PasswordValidators

User = get_user_model()


class UserRegistrationSerializer(BaseUserRegistrationSerializer):

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.number = user.id
        user.save()
        return user

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


class UserUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'date_of_birth', 'password', 'image']


class CurrentUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'date_of_birth', 'password', 'image']
