from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):

        User.objects.create_superuser(
            email='admin@yandex.ru',
            first_name='Admin',
            last_name='Adminov',
            password='123qwe456rty',
            date_of_birth="2024-01-25",
        )
