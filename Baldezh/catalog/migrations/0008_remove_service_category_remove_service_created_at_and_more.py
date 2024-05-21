# Generated by Django 5.0.6 on 2024-05-17 14:33

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_category_photo'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='category',
        ),
        migrations.RemoveField(
            model_name='service',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='service',
            name='creator',
        ),
        migrations.RemoveField(
            model_name='service',
            name='description',
        ),
        migrations.RemoveField(
            model_name='service',
            name='email',
        ),
        migrations.RemoveField(
            model_name='service',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='service',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='service',
            name='status',
        ),
        migrations.RemoveField(
            model_name='service',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='service',
            name='extra',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Дополнительно'),
        ),
        migrations.AlterField(
            model_name='service',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Название услуги'),
        ),
        migrations.AlterField(
            model_name='service',
            name='photo',
            field=models.ImageField(upload_to='media/products', verbose_name='Фото услуги'),
        ),
        migrations.AlterField(
            model_name='service',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='От какой цены услуга'),
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, max_length=255, null=True, unique=True, verbose_name='URL')),
                ('address', models.CharField(blank=True, max_length=255, null=True, verbose_name='Адрес')),
                ('description', models.TextField(verbose_name='Описание')),
                ('status', models.CharField(blank=True, choices=[('watching', 'Рассмотрение'), ('accepted', 'Принят'), ('denied', 'Отклонён')], default='watching', max_length=100, null=True, verbose_name='Статус страницы пользователя')),
                ('upper_in_top', models.BooleanField(default=False, verbose_name='Выше в топе')),
                ('category', models.ManyToManyField(blank=True, to='catalog.category', verbose_name='Категория')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='provider', to=settings.AUTH_USER_MODEL, verbose_name='Страница пользователя')),
            ],
        ),
        migrations.AddField(
            model_name='service',
            name='provider',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='services', to='catalog.provider', verbose_name='Кто предоставляет услуги'),
        ),
        migrations.AlterField(
            model_name='reviews',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='catalog.provider', verbose_name='Родительский пост'),
        ),
    ]