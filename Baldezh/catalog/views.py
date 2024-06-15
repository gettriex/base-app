from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from slugify import slugify

from catalog.forms import ReviewsForm, CreateServiceForm, BecomeProviderForm
from catalog.models import Category, Service, Reviews, Provider


# Create your views here.
class CatalogListView(ListView):
    model = Provider
    template_name = 'catalog/catalog.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        queryset = Provider.objects.filter(status='Принят').order_by('upper_in_top', 'user__username', 'updated_at')

        # Поиск по названию
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(user__first_name__icontains=query) | Q(user__patronymic__icontains=query) | Q(
                    user__last_name__icontains=query) | Q(description__icontains=query))

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


def get_categories(request):
    query = request.GET.get('query', '')
    if query:
        categories = Category.objects.filter(name__icontains=query)
    else:
        categories = Category.objects.all()

    category_list = [{'id': category.id, 'name': category.name} for category in categories]
    return JsonResponse(category_list, safe=False)


class ShowCategoryView(ListView):
    model = Provider
    template_name = 'catalog/catalog.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        return Provider.objects.filter(status='Принят',
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
        # Получаем объект поста
        service = self.object
        # Получаем текущего пользователя
        if self.request.user.is_authenticated:
            user = self.request.user
            context['reviews_form'] = ReviewsForm(initial={'user': user, 'parent': service})
            # Передаем текущего пользователя и объект поста в форму при ее создании
            context['user_has_review'] = self.object.reviews.filter(user=user).exists()
        return context

    def post(self, request, *args, **kwargs):
        form = ReviewsForm(request.POST)
        if form.is_valid():
            review = form.save()
            return redirect('catalog:detail', service_slug=review.parent.slug)
        else:
            return self.render_to_response(self.get_context_data(form=form))


class BecomeProvider(LoginRequiredMixin, CreateView):
    model = Provider
    form_class = BecomeProviderForm
    template_name = 'catalog/become-provider.html'
    success_url = reverse_lazy('catalog:index')

    def form_valid(self, form):
        # Получаем текущего пользователя
        user = self.request.user
        self.request.user.become_creator()
        # Устанавливаем значение поля 'creator' в экземпляре формы
        form.instance.user = user
        # Вызываем метод form_valid родительского класса
        return super().form_valid(form)


class ProviderEdit(UpdateView, LoginRequiredMixin):
    model = Provider
    template_name = 'catalog/become-provider.html'
    form_class = BecomeProviderForm

    def get_success_url(self):
        return reverse_lazy('catalog:index')

    def get_object(self, queryset=None):
        return Provider.objects.get(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Получаем объект поста
        service = self.object
        # Получаем текущего пользователя
        if self.request.user.is_authenticated:
            user = self.request.user
            context['reviews_form'] = ReviewsForm(initial={'user': user, 'parent': service})
            # Передаем текущего пользователя и объект поста в форму при ее создании
            context['user_has_review'] = self.object.reviews.filter(user=user).exists()
        return context


class CreateService(LoginRequiredMixin, CreateView):
    model = Service
    template_name = 'catalog/add_service.html'
    form_class = CreateServiceForm
    success_url = reverse_lazy('catalog:edit')

    def form_valid(self, form):
        # Получаем текущего пользователя

        user = Provider.objects.get(user=self.request.user)
        # Устанавливаем значение поля 'creator' в экземпляре формы
        form.instance.provider = user
        # Вызываем метод form_valid родительского класса
        return super().form_valid(form)


def delete_review(request, service_slug, pk):
    Reviews.objects.filter(pk=pk).delete()
    return redirect('catalog:detail', service_slug=service_slug)
