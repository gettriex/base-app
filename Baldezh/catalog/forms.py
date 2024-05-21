from django import forms

from catalog.models import Reviews, Service


class CreateServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = (
            'photo',
            'name',
            'price',
            'extra',
        )


class ReviewsForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ('parent', 'user', 'rating', 'comment')
        widgets = {
            'parent': forms.HiddenInput(),
            'user': forms.HiddenInput(),
            'comment': forms.Textarea(),
            'rating': forms.RadioSelect(),
        }