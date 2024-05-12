from django.contrib import admin
from django.contrib.auth import get_user_model
from django.utils.html import format_html


# Register your models here.
@admin.register(get_user_model())
class UserAdmin(admin.ModelAdmin):
    list_display = ('thumbnail', 'username', 'email', 'first_name', 'last_name')
    fields = ['photo', 'username', 'email', 'first_name', 'last_name', 'description']
    list_display_links = ['username', 'email', ]
    ordering = ['-date_joined']

    def thumbnail(self, obj):
        return format_html('<img src="{}" style="max-height: 50px; max-width: 50px;" />'.format(obj.photo.url))

    thumbnail.allow_tags = True
    thumbnail.short_description = 'Миниатюра'