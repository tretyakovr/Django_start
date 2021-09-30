from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now
from datetime import timedelta


class ShopUser(AbstractUser):
    avatar = models.ImageField(upload_to='user_avatars', blank=True)
    age = models.PositiveIntegerField(verbose_name='Возраст')
    sex = models.CharField(verbose_name='Пол', max_length=1, blank=True)
    email = models.CharField(verbose_name='e-mail', max_length=60, blank=True)
    activation_key = models.CharField(max_length=128, blank=True)
    activation_key_expires = models.DateTimeField(	default=(now() + timedelta(hours=48)))

    def is_activation_key_expired(self):
        if now() <= self.activation_key_expires:
            return False
        else:
            return True
