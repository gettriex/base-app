# Generated by Django 5.0.4 on 2024-05-05 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_service_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='service',
            options={'verbose_name': 'Объявление', 'verbose_name_plural': 'Объявления'},
        ),
        migrations.AlterField(
            model_name='service',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, null=True, unique=True, verbose_name='URL'),
        ),
    ]