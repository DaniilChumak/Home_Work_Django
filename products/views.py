from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from products.models import Product, Version
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView


class ProductListView(ListView):
    model = Product

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(CreateView):
    model = Product
    fields = ['name', 'description', 'image_preview', 'category', 'price']
    success_url = reverse_lazy('product:product_list')


class ProductUpdateView(UpdateView):
    model = Product
    fields = ['name', 'description', 'image_preview', 'category', 'price']
    success_url = reverse_lazy('product:product_list')

    def get_success_url(self):
        return reverse('product:product_detail', args=[self.kwargs.get('pk')])


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('product:product_list')


class VersionDetailView(DetailView):
    model = Version

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = Product.objects.get(pk=self.object.product.pk)
        context['product'] = product
        return context


class VersionDeleteView(LoginRequiredMixin, DeleteView):
    model = Version
    success_url = 'catalog/index.html'
    login_url = 'users:users_login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = Product.objects.get(pk=self.object.product.pk)
        context['product'] = product
        return context
