from django import forms

from catalog.models import Reviews, Service, Provider
from catalog.widgets import TagSelectWidget


class CreateServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = (
            'photo',
            'name',
            'price',
        )


class BecomeProviderForm(forms.ModelForm):
    class Meta:
        model = Provider
        fields = ('address', 'category', 'description', )
        widgets = {
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'category': TagSelectWidget(attrs={'class': 'form-control'}),
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