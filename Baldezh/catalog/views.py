from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView

# from catalog.forms import ReviewsForm
from catalog.models import Category, Service, Reviews


# Create your views here.
class CatalogListView(ListView):
    model = Service
    template_name = 'catalog/catalog.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class ShowCategoryView(ListView):
    model = Service
    template_name = 'catalog/catalog.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Service.objects.filter(category__slug=self.kwargs['cat_slug'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class ShowDetailView(DetailView):
    model = Service
    template_name = 'catalog/detail-view.html'
    slug_url_kwarg = 'service_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['reviews_form'] = ReviewsForm()
        return context