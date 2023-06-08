from django import forms
from .models import Order, OrderItem

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('shipping_address', 'payment_method')


class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ('product', 'quantity')
