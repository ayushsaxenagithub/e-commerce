from django.shortcuts import render, get_object_or_404, redirect
from .models import Review
from .forms import ReviewForm

def create_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect('review_detail', review_id=review.pk)
    else:
        form = ReviewForm()
    return render(request, 'review/create.html', {'form': form})

def review_detail(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    return render(request, 'review/detail.html', {'review': review})

def review_list(request):
    reviews = Review.objects.all()
    return render(request, 'review/list.html', {'reviews': reviews})

def update_review(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    form = ReviewForm(request.POST or None, instance=review)
    if form.is_valid():
        form.save()
        return redirect('review_detail', review_id=review.pk)
    return render(request, 'review/update.html', {'form': form, 'review': review})

def delete_review(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    if request.method == 'POST':
        review.delete()
        return redirect('review_list')
    return render(request, 'review/delete.html', {'review': review})
