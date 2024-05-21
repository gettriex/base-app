from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, DeleteView, CreateView

from catalog.forms import ReviewsForm, CreateServiceForm
from catalog.models import Category, Service, Reviews, Provider


# Create your views here.
class CatalogListView(ListView):
    model = Provider
    template_name = 'catalog/catalog.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        queryset = Provider.objects.filter(status='accepted').order_by('upper_in_top', 'user__username', 'updated_at')

        # Поиск по названию
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(name__icontains=query)

        # Фильтрация по цене
        min_price = self.request.GET.get('min_price')
        max_price = self.request.GET.get('max_price')
        if min_price and max_price:
            queryset = queryset.filter(price__gte=min_price, price__lte=max_price)

        sort_by_price = self.request.GET.get('sort_by_price')
        if sort_by_price == 'ascending':
            queryset = queryset.order_by('price')
        elif sort_by_price == 'descending':
            queryset = queryset.order_by('-price')

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class ShowCategoryView(ListView):
    model = Provider
    template_name = 'catalog/catalog.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        return Provider.objects.filter(status='accepted',
                                      category__slug=self.kwargs['cat_slug']).order_by('user',
                                                                                       'updated_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class ShowDetailView(DetailView):
    model = Provider
    template_name = 'catalog/detail-view1.html'
    slug_url_kwarg = 'service_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Получаем текущего пользователя
        user = self.request.user
        # Получаем объект поста
        service = self.object
        # Передаем текущего пользователя и объект поста в форму при ее создании
        context['reviews_form'] = ReviewsForm(initial={'user': user, 'parent': service})
        context['user_has_review'] = self.object.reviews.filter(user=user).exists()
        return context

    def post(self, request, *args, **kwargs):
        form = ReviewsForm(request.POST)
        if form.is_valid():
            review = form.save()
            return redirect('catalog:detail', service_slug=review.parent.slug)
        else:
            return self.render_to_response(self.get_context_data(form=form))


class CreateService(LoginRequiredMixin, CreateView):
    model = Service
    template_name = 'catalog/add_service.html'
    form_class = CreateServiceForm
    success_url = reverse_lazy('catalog:index')

    def form_valid(self, form):
        # Получаем текущего пользователя
        user = self.request.user
        # Устанавливаем значение поля 'creator' в экземпляре формы
        form.instance.creator = user
        # Вызываем метод form_valid родительского класса
        return super().form_valid(form)


def delete_review(request, service_slug, pk):
    Reviews.objects.filter(pk=pk).delete()
    return redirect('catalog:detail', service_slug=service_slug)
