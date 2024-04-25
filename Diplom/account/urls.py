
from django.contrib.auth.views import LogoutView
from django.urls import path

from . import views
from .views import Organisation, company_login, company_logout, product_list, product_create, product_update, product_delete

app_name = "account"

urlpatterns = [
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', views.UserCreation.as_view(), name='registration'),
    path('organisation/', Organisation, name='organisation'),
    path('login/company/', company_login, name='company_login'),
    path('logout/company/', company_logout, name='company_logout'),
    path('products/', product_list, name='product_list'),
    path('products/new/', product_create, name='product_create'),
    path('products/<int:pk>/edit/', product_update, name='product_update'),
    path('products/<int:pk>/delete/', product_delete, name='product_delete'),
]

