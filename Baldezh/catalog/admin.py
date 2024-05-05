from django.contrib import admin
from django.utils.html import format_html

from catalog.models import Service, Category, Reviews
from catalog.utils import confirm, deny


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('thumbnail',
                    'name',
                    'slug',
                    'price',
                    'creator',
                    'phone',
                    'email',
                    'average_rating',
                    'status',
                    'created_at',
                    'updated_at')
    fields = (
        'creator',
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
    ordering = ('-status', '-updated_at', '-created_at', 'name',)
    list_display_links = ('thumbnail', 'name')
    search_fields = ('name',)
    list_editable = ('status',)
    list_filter = ('status', 'created_at', 'updated_at',)
    actions = ('confirm_service', 'deny_service',)

    def thumbnail(self, obj):
        return format_html('<img src="{}" style="max-height: 50px; max-width: 50px;" />'.format(obj.photo.url))

    thumbnail.allow_tags = True
    thumbnail.short_description = 'Миниатюра'

    @admin.action(description='Принять объявления')
    def confirm_service(self, request, queryset):
        count = 0
        for obj in queryset:
            if obj.status != 'accepted':
                response = confirm(obj)
                if response:
                    count += 1

        self.message_user(request, f'Успешно приняты {count} объявлений')

    @admin.action(description='Отказать объявления')
    def deny_service(self, request, queryset):
        count = 0
        for obj in queryset:
            response = deny(obj)
            if response:
                count += 1
        self.message_user(request, f'Успешно отклонены {count} объявлений')


@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('parent', 'user', 'rating', 'comment')

    class Meta:
        # Задаем порядок моделей
        order = ['Category', 'Service', 'Review']
