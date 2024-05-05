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
    creator = models.ForeignKey(get_user_model(), models.CASCADE, verbose_name='Создатель поста',
                                related_name='creator', null=True, blank=True)
    name = models.CharField("Название объявления", max_length=100)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL", null=True, blank=True)
    category = models.ManyToManyField(Category, blank=True, verbose_name="Категория")
    description = models.TextField("Описание")
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2)
    photo = models.ImageField("Фото", upload_to='media/products')
    phone = models.CharField("Телефон", max_length=15, null=True, blank=True)
    email = models.EmailField("Почта", max_length=25)
    status = models.CharField("Статус услуги", max_length=100, null=True, blank=True,
                              choices=(("watching", "Рассмотрение"),
                                       ("accepted", "Принят"),
                                       ("denied", "Отклонён")),
                              default="watching")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата отправки', blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления', blank=True, null=True)

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"

    def __str__(self):
        return f'{self.name}'

    def change_status_to_accepted(self):
        self.status = 'accepted'
        self.save()

    def change_status_to_denied(self):
        self.status = 'denied'
        self.save()

    def average_rating(self):
        reviews = self.reviews.all()
        if reviews:
            total_ratings = sum(review.rating for review in reviews)
            average = total_ratings / len(reviews)
            return round(average, 1)
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
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата отправки', blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления', blank=True, null=True)

    def __str__(self):
        return f"{self.parent} - {self.user}"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
