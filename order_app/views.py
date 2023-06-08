from django.shortcuts import render, redirect, get_object_or_404
from .forms import OrderForm, OrderItemForm
from .models import Order, OrderItem

def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()
            return redirect('order_detail', pk=order.pk)
    else:
        form = OrderForm()
    return render(request, 'order/create_order.html', {'form': form})


def order_detail(request, pk):
    order = Order.objects.get(pk=pk)
    return render(request, 'order/order_detail.html', {'order': order})


def create_order_item(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    if request.method == 'POST':
        form = OrderItemForm(request.POST)
        if form.is_valid():
            order_item = form.save(commit=False)
            order_item.order = order
            order_item.save()
            return redirect('order_detail', pk=order.pk)
    else:
        form = OrderItemForm()
    return render(request, 'order/create_order_item.html', {'form': form, 'order': order})


def update_order_item(request, order_id, item_id):
    order = get_object_or_404(Order, pk=order_id)
    order_item = get_object_or_404(OrderItem, pk=item_id, order=order)
    if request.method == 'POST':
        form = OrderItemForm(request.POST, instance=order_item)
        if form.is_valid():
            form.save()
            return redirect('order_detail', pk=order.pk)
    else:
        form = OrderItemForm(instance=order_item)
    return render(request, 'order/update_order_item.html', {'form': form, 'order': order, 'order_item': order_item})


def delete_order_item(request, order_id, item_id):
    order = get_object_or_404(Order, pk=order_id)
    order_item = get_object_or_404(OrderItem, pk=item_id, order=order)
    if request.method == 'POST':
        order_item.delete()
        return redirect('order_detail', pk=order.pk)
    return render(request, 'order/delete_order_item.html', {'order': order, 'order_item': order_item})
