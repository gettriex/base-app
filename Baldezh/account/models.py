from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    patronymic = models.CharField(max_length=100, blank=True, null=True, verbose_name='Отчество')
    photo = models.ImageField(upload_to="users/", default="users/default-profile.jpg",
                              blank=True, null=True, verbose_name='Фотография')
    telephone = models.CharField(max_length=20, default=None, blank=True, null=True, verbose_name='Номер телефона')
    description = models.TextField(default=None, blank=True, null=True, verbose_name='О себе')
    is_creator = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username