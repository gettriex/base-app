from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, UpdateView

from account.forms import LoginUserForm, CustomUserCreationForm, UserEditForm
from catalog.models import Service


# Create your views here.
class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'account/authorization.html'
    context_object_name = 'login'


class UserCreation(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'account/registration.html'
    context_object_name = 'registration'
    success_url = reverse_lazy('account:login')


class UserProfile(TemplateView):
    template_name = 'account/profile.html'

    def get_success_url(self):
        return reverse_lazy('account:profile', args=[self.request.user.id])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['services'] = Service.objects.filter(creator=self.request.user)
        return context


class UserEdit(UpdateView, LoginRequiredMixin):
    model = get_user_model()
    template_name = 'account/cabinet.html'
    form_class = UserEditForm

    def get_success_url(self):
        return reverse_lazy('catalog:index')

    def get_object(self, queryset=None):
        return get_user_model().objects.get(pk=self.request.user.pk)


