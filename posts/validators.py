from datetime import datetime

from rest_framework.serializers import ValidationError


class TitleValidators:

    def __init__(self, fields):
        self.fields = fields

    def __call__(self, value):
        title = dict(value).get(self.fields[0])
        words = ('ерунда', 'глупость', 'чепуха')
        for word in words:
            if word in title:
                raise ValidationError('заголовок содержит запрещенные слова: ерунда, глупость, чепуха')
#
#
# class AuthorValidators:
#
#     def __init__(self, fields):
#         self.fields = fields
#
#     def __call__(self, value):
#         author = dict(value).get(self.fields[0])
#         if (datetime.now() - author.date_of_birth) < 18:
#             raise ValidationError('что автор поста не достиг возраста 18 лет')
