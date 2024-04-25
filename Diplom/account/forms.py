from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm

from account.models import User, Company


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(
        attrs={'class': 'form-input', 'placeholder': 'Логин/Почта'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(
        attrs={'class': 'form-input', 'id': 'password-input', 'placeholder': 'Пароль'}))

    class Meta:
        model = get_user_model()
        fields = ['username', 'password']


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(
        attrs={'class': 'form-input', 'placeholder': 'Логин'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(
        attrs={'class': 'form-input', 'id': 'password-input', 'placeholder': 'Пароль'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(
        attrs={'class': 'form-input', 'placeholder': 'Повтор пароля'}))

    # Поле для фото
    photo = forms.ImageField(label='Фото', required=False, widget=forms.FileInput(
        attrs={'class': 'form-input', 'id': 'input__file', 'type': 'file'}))  # Убираем атрибут hidden

    email = forms.EmailField(label='E-mail', widget=forms.EmailInput(
        attrs={'class': 'form-input', 'placeholder': 'E-mail'}))

    class Meta:
        model = get_user_model()
        fields = ['username', 'password1', 'password2', 'photo', 'email', ]
        labels = {
            'email': 'E-mail',
            'photo': 'Фото'
        }

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Такой E-mail уже существует!")
        return email


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'password', 'photo', 'email',)


class CompanyRegistrationForm(forms.ModelForm):
    password_confirmation = forms.CharField(widget=forms.PasswordInput(), label='Подтверждение пароля')

    class Meta:
        model = Company
        fields = ['organization_name', 'inn', 'email', 'username', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirmation = cleaned_data.get("password_confirmation")

        if password != password_confirmation:
            raise forms.ValidationError("Пароли не совпадают")

        return cleaned_data


class CompanyLoginForm(forms.Form):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        try:
            company = Company.objects.get(username=username)
        except Company.DoesNotExist:
            raise forms.ValidationError("Неверный логин или пароль")

        if not company.password == password:
            raise forms.ValidationError("Неверный логин или пароль")

        return self.cleaned_data
