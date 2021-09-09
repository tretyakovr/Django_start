from django.db import models
from django.contrib.auth.models import AbstractUser


class ShopUser(AbstractUser):
    avatar = models.ImageField(upload_to='user_avatars', blank=True)
    age = models.PositiveIntegerField(verbose_name='Возраст')
    sex = models.CharField(verbose_name='Пол', max_length=1, blank=True)
    email = models.CharField(verbose_name='e-mail', max_length=60, blank=True)
