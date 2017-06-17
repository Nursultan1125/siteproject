# coding=utf-8
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Users(models.Model):
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    users_user = models.OneToOneField(User, verbose_name='Пользователь')
    users_city = models.CharField(max_length=255, verbose_name='Ваш город', null=True)

    def __str__(self):
        return self.users_user.first_name
