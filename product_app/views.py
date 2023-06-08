from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Product

class ProductListView(ListView):
    model = Product
    template_name = 'product_app/product_list.html'
    context_object_name = 'products'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        # Apply any filtering or sorting logic as needed
        return queryset

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_app/product_detail.html'
    context_object_name = 'product'

class ProductCreateView(CreateView):
    model = Product
    template_name = 'product_app/product_create.html'
    fields = '__all__'

class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'product_app/product_update.html'
    fields = '__all__'

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product_app/product_delete.html'
    success_url = reverse_lazy('product_app:product_list')
