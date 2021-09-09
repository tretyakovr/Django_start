from django.core.management.base import BaseCommand
from authapp.models import ShopUser


class Command(BaseCommand):
    def handle(self, *args, **options):
        # Создаем суперпользователя при помощи менеджера модели
        super_user = ShopUser.objects.create_superuser('admin', 'admin@wlocal', 'zaq1@WSX', age=21)
