from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Cart
from .forms import CartForm
# from ml_models import ml_prediction  

class CartListView(ListView):
    model = Cart
    template_name = 'cart_app/cart_list.html'
    context_object_name = 'carts'


class CartDetailView(DetailView):
    model = Cart
    template_name = 'cart_app/cart_detail.html'
    context_object_name = 'cart'


class CartCreateView(CreateView):
    model = Cart
    form_class = CartForm
    template_name = 'cart_app/cart_form.html'
    success_url = reverse_lazy('cart_app:cart_list')


class CartUpdateView(UpdateView):
    model = Cart
    form_class = CartForm
    template_name = 'cart_app/cart_form.html'
    success_url = reverse_lazy('cart_app:cart_list')


class CartDeleteView(DeleteView):
    model = Cart
    template_name = 'cart_app/cart_confirm_delete.html'
    success_url = reverse_lazy('cart_app:cart_list')
