from django import forms

from catalog.models import Reviews, Service, Provider, Category
from catalog.widgets import TagSelectWidget


class CreateServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = (
            'photo',
            'name',
            'price',
        )
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Название услуги', 'pattern': r'^[А-Яа-яЁё]+$'}),
        }


class BecomeProviderForm(forms.ModelForm):
    # category = forms.ModelMultipleChoiceField(
    #     queryset=Category.objects.all(),
    #     widget=TagSelectWidget(attrs={'class': 'form-control'}),
    #     required=False
    # )

    class Meta:
        model = Provider
        fields = ('best_time_start', 'best_time_end', 'address', 'category', 'description',)
        widgets = {
            'best_time_start': forms.TimeInput(attrs={'type': 'time'}),
            'best_time_end': forms.TimeInput(attrs={'type': 'time'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Адрес'}),
            'category': forms.SelectMultiple(attrs={}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }


class ReviewsForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ('parent', 'user', 'rating', 'comment')
        widgets = {
            'parent': forms.HiddenInput(),
            'user': forms.HiddenInput(),
            'comment': forms.Textarea(),
            'rating': forms.RadioSelect(attrs={'id': 'star', 'required': 'required'}, ),
        }
