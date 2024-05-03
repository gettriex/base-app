from django.urls import path
from . import views

urlpatterns = [
    path('', views.CatalogListView.as_view(), name='index'),
    path('category/<slug:cat_slug>/', views.ShowCategoryView.as_view(), name='category'),
    path('detail/<slug:service_slug>/', views.ShowDetailView.as_view(), name='detail'),
]

app_name = 'catalog'