from django import forms
from .models import CartItem

class CartForm(forms.ModelForm):
    class Meta:
        model = CartItem
        fields = ('product', 'quantity')

    def clean_quantity(self):
        quantity = self.cleaned_data['quantity']
        if quantity <= 0:
            raise forms.ValidationError("Quantity must be greater than zero.")
        return quantity
