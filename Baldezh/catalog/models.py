from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from slugify import slugify


# Create your models here.
class Category(models.Model):
    name = models.CharField("Название категории", max_length=100, unique=True, )
    # slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL", blank=True, null=True)
    slug = models.SlugField(max_length=80, unique=True, null=True, db_index=True, verbose_name="URL")
    photo = models.ImageField(upload_to="category/", null=True, blank=True, default='category/default.jpg')

    class Meta:
        db_table = 'category'
        verbose_name = "Категорию"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwards={'cat_slug': self.slug})


class Provider(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name='Страница пользователя',
                             related_name='provider', null=True, blank=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL", null=True, blank=True)
    best_time_start = models.TimeField(null=True, blank=True)
    best_time_end = models.TimeField(null=True, blank=True)
    address = models.CharField(max_length=255, verbose_name='Адрес местонахождения', null=True, blank=True)
    category = models.ManyToManyField(Category, blank=True, verbose_name="Категория")
    description = models.TextField("Описание")
    status = models.CharField("Статус страницы пользователя", max_length=100, null=True, blank=True,
                              choices=(("Рассмотрение", "Рассмотрение"),
                                       ("Принят", "Принят"),
                                       ("Отклонён", "Отклонён")),
                              default="Рассмотрение")
    upper_in_top = models.BooleanField(default=False, verbose_name="Выше в топе")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"

    def __str__(self):
        return f'{self.user.fio()}'

    def change_status_to_accepted(self):
        self.status = 'Принят'
        self.save()

    def change_status_to_denied(self):
        self.status = 'Отклонён'
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

    def get_all_services(self):
        services = self.services.all()
        if services:
            return services
        else:
            return 0

    def get_all_categories(self):
        categories = self.category.all()
        if categories:
            return categories
        else:
            return 0

    def get_absolute_url(self):
        return reverse('category', kwards={'cat_slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)

        super().save(*args, **kwargs)


class Service(models.Model):
    provider = models.ForeignKey(Provider, models.CASCADE, verbose_name='Кто предоставляет услуги',
                                 related_name='services', null=True, blank=True)
    photo = models.ImageField("Фото услуги", upload_to='media/products')
    name = models.CharField("Название услуги", max_length=100)
    price = models.DecimalField("От какой цены услуга", max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"

    def __str__(self):
        return f'{self.name}'

    def get_price(self):
        return f'{round(self.price)}'


class Reviews(models.Model):
    parent = models.ForeignKey(
        'Provider', on_delete=models.CASCADE, related_name='reviews', verbose_name="Родительский пост"
    )
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name="Пользователь")
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)], default=5)
    comment = models.TextField("Сообщение", max_length=5000, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата отправки', blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления', blank=True, null=True)

    def __str__(self):
        return f"{self.parent} - {self.user}"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
