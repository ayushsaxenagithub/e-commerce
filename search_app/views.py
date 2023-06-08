from django.shortcuts import render
from .forms import SearchForm
from .models import ProductSearch

def search_view(request):
    form = SearchForm(request.GET)
    results = []
    
    if form.is_valid():
        query = form.cleaned_data['query']
        
        # Get the search results from the database
        products = ProductSearch.objects.all()
        product_names = [product.name for product in products]
        
        # Perform search or any other necessary processing
        
        # Add your search logic here
        
        results = products  # Placeholder for search logic
        
    context = {
        'form': form,
        'results': results
    }
    
    return render(request, 'search_app/search.html', context)
