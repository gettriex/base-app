from django.urls import path
from . import views

urlpatterns = [
    path('', views.CatalogListView.as_view(), name='index'),
    path('create-service', views.CreateService.as_view(), name='create_service'),
    path('category/<slug:cat_slug>/', views.ShowCategoryView.as_view(), name='category'),
    path('service/<slug:service_slug>/', views.ShowDetailView.as_view(), name='detail'),
    path('service/<slug:service_slug>/delete-review/<int:pk>', views.delete_review, name='delete_review'),
    path('become-provider/', views.BecomeProvider.as_view(), name='become_provider'),
    path('get-categories/', views.get_categories, name='get-categories'),
]

app_name = 'catalog'
