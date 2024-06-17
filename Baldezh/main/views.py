from django.shortcuts import render
from django.views.generic import TemplateView

from catalog.models import Category, Provider


# Create your views here.
class IndexView(TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['specialists'] = Provider.objects.all()[:6]
        context['categories'] = Category.objects.all()
        return context