from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# class CustomUser(AbstractBaseUser):
#     password = models.CharField(verbose_name='Пароль', max_length=128)
#     last_login = models.DateTimeField(verbose_name='Время последней авторизации', auto_now=True)
#     is_superuser = models.BooleanField(verbose_name='Является администратором', )
#     username = models.CharField(verbose_name='Имя пользователя', max_length=100)
#     realname = models.CharField(verbose_name='Имя', max_length=100)
#     surname = models.CharField(verbose_name='Фамилия', max_length=100)
#     is_staff = models.BooleanField(verbose_name='Является модератором', )
#     is_active = models.BooleanField(verbose_name='Является активным', )
#     date_joined = models.DateTimeField(verbose_name='Время регистрации', auto_now_add=True)

#     def __str__(self):
#         return self.username