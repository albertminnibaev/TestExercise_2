from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models

from posts.models import NULLABLE
from users.managers import UserManager


class User(AbstractBaseUser):

    username = None

    first_name = models.CharField(max_length=100, verbose_name='имя пользователя')
    last_name = models.CharField(max_length=100, verbose_name='фамилия пользователя')
    email = models.EmailField(unique=True, verbose_name='адрес электронной почты')
    image = models.ImageField(upload_to='users/', default='users/avatar_default.jpeg', verbose_name='аватар',
                              **NULLABLE)
    date_of_birth = models.DateField(verbose_name='дата рождения')
    created_at = models.DateField(auto_now_add=True, verbose_name='дата создания')
    date_of_change = models.DateField(auto_now=True, verbose_name='дата редактирования')
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    # эта константа определяет поле для логина пользователя
    USERNAME_FIELD = 'email'

    # эта константа содержит список с полями,
    # которые необходимо заполнить при создании пользователя
    REQUIRED_FIELDS = ['first_name', 'last_name', 'date_of_birth']

    # также для работы модели пользователя должен быть переопределен
    # менеджер объектов
    objects = UserManager()
    #
    # @property
    # def is_active(self):
    #     return self.is_active
    #
    # @property
    # def is_staff(self):
    #     return self.is_staff
    #
    # @property
    # def is_superuser(self):
    #     return self.is_superuser
    #
    # @property
    # def is_admin(self):
    #     return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

    def __str__(self):
        return f'{self.first_name}, {self.last_name} ({self.email})'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
