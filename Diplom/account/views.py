from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from account.forms import CustomUserCreationForm, CompanyRegistrationForm, CompanyLoginForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Product
from .forms import LoginUserForm


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'account/authorization.html'
    extra_context = {'title': 'Авторизация'}

    def get_success_url(self):
        return reverse_lazy('home')


class UserCreation(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'account/register.html'
    context_object_name = 'registration'
    success_url = reverse_lazy('account:registration')


class Organisetion(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'account/login.html'
    context_object_name = 'registration'
    success_url = reverse_lazy('account:login')


def logout_user(request):
    logout(request)
    return redirect('login')


def Organisation(request):
    if request.method == 'POST':
        form = CompanyRegistrationForm(request.POST)
        if form.is_valid():
            company = form.save(commit=False)
            company.password = form.cleaned_data['password']  # Сохраняйте пароль как есть, или используйте шифрование
            company.save()
            return redirect('home')
    else:
        form = CompanyRegistrationForm()
    return render(request, 'account/login.html', {'form': form})


def company_login(request):
    if request.method == 'POST':
        form = CompanyLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            request.session['username'] = username  # Сохраняем имя пользователя в сессию
            return redirect('home')  # Перенаправление на защищенную страницу
    else:
        form = CompanyLoginForm()

    return render(request, 'account/company_login.html', {'form': form})


def company_logout(request):
    if 'username' in request.session:
        del request.session['username']  # Удаляем имя пользователя из сессии
    return redirect('company_login')  # Перенаправляем на страницу входа


def is_company(user):
    return user.is_company


@login_required
@user_passes_test(is_company)
def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'account/product_form.html', {'form': form})


@login_required
def product_list(request):
    products = Product.objects.all()
    return render(request, 'account/product_list.html', {'products': products})


@login_required
@user_passes_test(is_company)
def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.created_by = request.user
            product.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'account/product_form.html', {'form': form})

def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    return redirect('product_list')

