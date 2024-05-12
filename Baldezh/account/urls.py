from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', views.UserCreation.as_view(), name='registration'),
    path('profile/', views.UserProfile.as_view(), name='profile'),
    path('profile/edit/', views.UserEdit.as_view(), name='edit'),
]

app_name = 'account'