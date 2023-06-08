from django.shortcuts import render, redirect
from .models import Wishlist
from .forms import WishlistForm

def wishlist(request):
    user = request.user
    wishlist_items = Wishlist.objects.filter(user=user)
    context = {'wishlist_items': wishlist_items}
    return render(request, 'wishlist/wishlist.html', context)

def add_to_wishlist(request, product_id):
    user = request.user
    product = Product.objects.get(pk=product_id)
    wishlist_item, created = Wishlist.objects.get_or_create(user=user, product=product)
    if created:
        # Wishlist item was successfully created
        # Add any additional logic or messages
        pass
    return redirect('wishlist')

def remove_from_wishlist(request, wishlist_id):
    wishlist_item = Wishlist.objects.get(pk=wishlist_id)
    wishlist_item.delete()
    # Add any additional logic or messages
    return redirect('wishlist')
