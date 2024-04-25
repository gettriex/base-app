from django.contrib.auth import get_user_model
from django.db import models


# Create your models here.


# class Suppliers(models.Model):
#     category = models.ManyToManyField("Category", max_length=255, unique=True, on_delete=models.CASCADE)
#     slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL", blank=True, null=True)
#
#     class Meta:
#         db_table = 'suppliers'
#         verbose_name = 'Поставщик услуги'
#         verbose_name_plural = 'Поставщик услуг'
#
#     def __str__(self):
#         return self.category
