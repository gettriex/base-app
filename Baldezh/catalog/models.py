from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


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
    name = models.CharField("Название объявления", max_length=100)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    category = models.ManyToManyField(Category, blank=True, verbose_name="Категория")
    description = models.TextField("Описание")
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2)
    photo = models.ImageField("Фото", upload_to='media/products')
    phone = models.CharField("Телефон", max_length=15, null=True, blank=True)
    email = models.EmailField("Почта", max_length=25)

    class Meta:
        verbose_name = "Услугу"
        verbose_name_plural = "Услуги"

    def __str__(self):
        return f'{self.name}'

    def average_rating(self):
        reviews = self.reviews.all()
        if reviews:
            total_ratings = sum(review.rating for review in reviews)
            return total_ratings / len(reviews)
        else:
            return 0

    def count_rating(self):
        reviews = self.reviews.all()
        if reviews:
            return len(reviews)
        else:
            return 0

    def get_absolute_url(self):
        return reverse('category', kwards={'cat_slug': self.slug})


class Reviews(models.Model):
    parent = models.ForeignKey(
        'Service', on_delete=models.CASCADE, related_name='reviews', verbose_name="Родительский пост"
    )
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name="Пользователь")
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    comment = models.TextField("Сообщение", max_length=5000, null=True, blank=True)

    def __str__(self):
        return f"{self.parent} - {self.user}"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"