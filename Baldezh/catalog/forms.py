from django import forms

from catalog.models import Reviews


# class ReviewsForm(forms.ModelForm):
#     class Meta:
#         model = Reviews
#         fields = ('parent', 'user', 'rating', 'comment')
#         widgets = {
#             'parent': forms.HiddenInput(),
#             'user': forms.HiddenInput(),
#             'comment': forms.Textarea(attrs={'class': 'form-control'}),
#             'rating': forms.ChoiceField(attrs={'class': 'form-control'}),
#         }