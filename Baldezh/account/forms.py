from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(
        attrs={'class': 'input-control', 'placeholder': 'Логин/Почта'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(
        attrs={'class': 'input-control', 'id': 'password-input', 'placeholder': 'Пароль'}))

    class Meta:
        model = get_user_model()
        fields = ['username', 'password']


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(
        attrs={'class': 'input-control', 'placeholder': 'Логин'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(
        attrs={'class': 'input-control', 'id': 'password-input', 'placeholder': 'Пароль'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(
        attrs={'class': 'input-control', 'placeholder': 'Повтор пароля'}))

    class Meta:
        model = get_user_model()
        fields = ['username', 'password1', 'password2', 'email', ]
        labels = {
            'email': 'E-mail',
        }
        widgets = {
            'email': forms.TextInput(attrs={'class': 'input-control', 'placeholder': 'E-mail'}),
        }

    def clean_email(self):
        email = self.cleaned_data['email']
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError("Такой E-mail уже существует!")
        return email


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'password', 'email',)