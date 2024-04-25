import uuid
from audioop import reverse

from django.db import models


# from account.models import Company


# Create your models here.


class Category(models.Model):
    name = models.CharField("Название категории", max_length=100, unique=True, )
    # slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL", blank=True, null=True)
    slug = models.SlugField(max_length=80, unique=True, null=True, db_index=True, verbose_name="URL")

    class Meta:
        db_table = 'category'
        verbose_name = "Категорию"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwards={'cat_slug': self.slug})


class Service(models.Model):
    name = models.CharField("ФИО", max_length=100)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    description = models.TextField("Описание")
    photo = models.ImageField("Фото", upload_to='media/products')
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2)
    category = models.ManyToManyField(Category, blank=True, verbose_name="Категория")

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('category', kwards={'cat_slug': self.slug})


class Reviews(models.Model):
    email = models.EmailField()
    name = models.CharField("Имя", max_length=100)
    text = models.TextField("Сообщение", max_length=5000)
    parent = models.ForeignKey(
        'self', blank=True, null=True, on_delete=models.SET_NULL, verbose_name="Родитель"
    )

    # company = models.ForeignKey(Company, verbose_name="компания", on_delete=models.CASCADE)

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.company = None

    def __str__(self):
        return f"{self.name} - {self.company}"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

# class Tag(models.Model):
#     tag = models.CharField(max_length=100, db_index=True)
#     slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
#
#     def __str__(self):
#         return self.tag
