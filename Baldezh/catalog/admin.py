from django.contrib import admin

from catalog.models import Service, Category, Reviews


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'slug',
                    'description',
                    'price',
                    'photo',
                    'phone',
                    'email',
                    'average_rating')
    fields = (
        'name',
        'slug',
        'category',
        'description',
        'price',
        'photo',
        'phone',
        'email'
    )
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('parent', 'user', 'rating', 'comment')

    class Meta:
        # Задаем порядок моделей
        order = ['Category', 'Service', 'Review']
