from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'catalog'

urlpatterns = [
    path('', views.IndexListView.as_view(), name='index'),
    path('category/<slug:cat_slug>/', views.ShowCategoryView.as_view(), name='category'),
    path('service/', views.AddCategoryView.as_view(), name='add_service'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
