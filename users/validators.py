import re
from rest_framework.serializers import ValidationError


class EmailValidators:

    def __init__(self, fields):
        self.fields = fields

    def __call__(self, value):
        email = dict(value).get(self.fields[0])
        if not bool(re.search(r'(@mail.ru)|(@yandex.ru)', email)):
            raise ValidationError('разрешены только домены: mail.ru, yandex.ru')


class PasswordValidators:

    def __init__(self, fields):
        self.fields = fields

    def __call__(self, value):
        password = dict(value).get(self.fields[0])
        if len(password) < 8:
            raise ValidationError('пароль должен быть не менее 8 символов')
        if not bool(re.search(r'\d', password)):
            raise ValidationError('пароль должен включать цифры')
