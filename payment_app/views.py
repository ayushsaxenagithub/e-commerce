from django.shortcuts import render, get_object_or_404, redirect
from .models import Payment
from .forms import PaymentForm

def payment_list(request):
    payments = Payment.objects.all()
    return render(request, 'payment/list.html', {'payments': payments})

def payment_detail(request, pk):
    payment = get_object_or_404(Payment, pk=pk)
    return render(request, 'payment/detail.html', {'payment': payment})

def payment_create(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('payment_list')
    else:
        form = PaymentForm()
    return render(request, 'payment/create.html', {'form': form})

def payment_update(request, pk):
    payment = get_object_or_404(Payment, pk=pk)
    if request.method == 'POST':
        form = PaymentForm(request.POST, instance=payment)
        if form.is_valid():
            form.save()
            return redirect('payment_list')
    else:
        form = PaymentForm(instance=payment)
    return render(request, 'payment/update.html', {'form': form})

def payment_delete(request, pk):
    payment = get_object_or_404(Payment, pk=pk)
    if request.method == 'POST':
        payment.delete()
        return redirect('payment_list')
    return render(request, 'payment/delete.html', {'payment': payment})
