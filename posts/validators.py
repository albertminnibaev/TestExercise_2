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
