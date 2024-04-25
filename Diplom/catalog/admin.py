from django.contrib import admin

from catalog.forms import ReviewForm
from catalog.models import Service, Category, Reviews


# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Reviews)
class CompanyAdmin(admin.ModelAdmin):
    add_form = ReviewForm
    model = Reviews
    list_display = ['email', 'name']


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
