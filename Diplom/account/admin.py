from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from account.forms import CustomUserCreationForm, CustomUserChangeForm, CompanyRegistrationForm
from account.models import User, Company


# Register your models here.
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ['email', 'username']

# class CompanyAdmin(admin.ModelAdmin):
#     # Определяем формы для создания и изменения записей
#     add_form = CompanyRegistrationForm
#     form = CompanyRegistrationForm
#
#     # Определяем отображаемые поля в списке записей
#     list_display = ['organization_name', 'username', 'email']


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    add_form = CompanyRegistrationForm
    model = Company
    list_display = ['organization_name', 'username']
