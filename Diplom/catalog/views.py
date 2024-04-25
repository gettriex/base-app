from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from catalog.forms import ServiceForm
from catalog.models import Service, Category


# Create your views here.


class IndexListView(ListView):
    model = Service
    template_name = 'catalog/catalog.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['test'] = 'Хоть что'
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

class AddCategoryView(CreateView):
    model = Service
    template_name = 'catalog/add_service.html'
    form_class = ServiceForm
    success_url = reverse_lazy('catalog:index')

# def add_service(request):
#     if request.method == 'POST':
#         form = ServiceForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         form = ServiceForm()
#     return render(request, 'catalog/add_service.html', {'form': form})
