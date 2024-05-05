from django import forms

from catalog.models import Reviews, Service


class CreateServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ('creator',
                  'name',
                  'category',
                  'description',
                  'price',
                  'photo',
                  'phone',
                  'email',
                  )

        widgets = {
            'creator': forms.HiddenInput()
        }


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