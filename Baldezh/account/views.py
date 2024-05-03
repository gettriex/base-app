from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView

from account.forms import LoginUserForm, CustomUserCreationForm


# Create your views here.
class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'account/authorization.html'
    context_object_name = 'login'


class UserCreation(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'account/authorization.html'
    context_object_name = 'registration'
    success_url = reverse_lazy('account:login')