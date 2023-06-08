from django.contrib import admin
from .models import Review
from django.http import HttpResponse
import csv


class ReviewAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'product', 'rating', 'created_at']
    actions = ['download_reviews']

    def download_reviews(self, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="reviews.csv"'
        writer = csv.writer(response)
        writer.writerow(['Title', 'User', 'Product', 'Rating', 'Created At'])
        for review in queryset:
            writer.writerow([review.title, review.user.username, review.product.name, review.rating, review.created_at])
        return response

    download_reviews.short_description = 'Download selected reviews as CSV'

admin.site.register(Review, ReviewAdmin)
