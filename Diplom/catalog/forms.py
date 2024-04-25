from django import forms

from .models import Reviews, Service


class ReviewForm(forms.ModelForm):
    """Форма отзывов"""
    class Meta:
        model = Reviews
        fields = ("name", "email", "text")


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        # fields = "__all__"
        fields = ("name", "slug", "description", "photo", "price", "category")
