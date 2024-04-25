
from django.contrib import admin
from django.urls import path, include

from account import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('catalog/', include('catalog.urls', namespace='catalog')),
    path('account/', include('account.urls', namespace='account')),
]

