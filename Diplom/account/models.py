from django.contrib.auth.models import AbstractUser
from django.db import models

from Diplom import settings


# Create your models here.
class User(AbstractUser):
    photo = models.ImageField(upload_to='users/%Y/%m/%d/', default=None, blank=True, null=True,
                              verbose_name='Фотография')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username


class Company(models.Model):
    organization_name = models.CharField(max_length=100, verbose_name='Наименование организации')
    inn = models.CharField(max_length=12, verbose_name='ИНН')
    email = models.EmailField(verbose_name='Электронная почта')
    username = models.CharField(max_length=50, verbose_name='Логин')
    password = models.CharField(max_length=50, verbose_name='Пароль')

    def __str__(self):
        return self.organization_name

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    created_by = models.ForeignKey('User', on_delete=models.CASCADE, related_name='products', verbose_name="Создано пользователем")

    def __str__(self):
        return self.name
