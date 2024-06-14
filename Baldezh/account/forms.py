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
        attrs={'class': 'input-control', 'id': 'input-control', 'placeholder': 'Пароль'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(
        attrs={'class': 'input-control', 'placeholder': 'Повтор пароля'}))

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'patronymic', 'username', 'password1', 'password2', 'email', ]
        labels = {
            'email': 'E-mail',
        }
        widgets = {
            'email': forms.TextInput(attrs={'class': 'input-control', 'placeholder': 'E-mail'}),
            'first_name': forms.TextInput(attrs={'class': 'input-control', 'placeholder': 'Имя', 'pattern': r'^[А-Яа-яЁё]+$'}),
            'last_name': forms.TextInput(attrs={'class': 'input-control', 'placeholder': 'Фамилия', 'pattern': r'^[А-Яа-яЁё]+$'}),
            'patronymic': forms.TextInput(attrs={'class': 'input-control', 'placeholder': 'Отчество', 'pattern': r'^[А-Яа-яЁё]+$'}),
        }

        def clean_email(self):
            email = self.cleaned_data['email']
            if get_user_model().objects.filter(email=email).exists():
                raise forms.ValidationError("Такой E-mail уже существует!")
            return email


class UserEditForm(forms.ModelForm):
    username = forms.CharField(disabled=True, label='Логин',
                               widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.CharField(disabled=True, label='Эл.Почта', widget=forms.TextInput(attrs={'class': 'form-input'}))
    photo = forms.FileField(label='Фото', widget=forms.FileInput(attrs={'class': 'form-input',
                                                                            'accept': "image/*"}))

    class Meta:
        model = get_user_model()

        fields = ['first_name', 'last_name', 'patronymic', 'username', 'email', 'telephone', 'photo']
        labels = {
            'email': 'E-mail',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-input', 'pattern': r'^[А-Яа-яЁё]+$'}),
            'last_name': forms.TextInput(attrs={'class': 'form-input', 'pattern': r'^[А-Яа-яЁё]+$'}),
            'patronymic': forms.TextInput(attrs={'class': 'form-input', 'pattern': r'^[А-Яа-яЁё]+$'}),
            'telephone': forms.TextInput(attrs={'class': 'form-input'}),
            'photo': forms.FileInput(attrs={'class': 'form-input',
                                            'accept': "image/*"}),
            'email': forms.TextInput(attrs={'class': 'input-control', 'placeholder': 'E-mail'}),
        }


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'password', 'email',)
