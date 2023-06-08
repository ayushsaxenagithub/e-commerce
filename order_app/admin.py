from django.contrib import admin
from django.http import HttpResponse
from .models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'status', 'created_at', 'updated_at')
    list_filter = ('status', 'created_at', 'updated_at')
    search_fields = ('id', 'user__username')
    actions = ['download_orders']

    def download_orders(self, request, queryset):
        """
        Custom action to download selected orders as a CSV file.
        """
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="orders.csv"'

        writer = csv.writer(response)
        writer.writerow(['Order ID', 'User', 'Status', 'Created At', 'Updated At'])

        for order in queryset:
            writer.writerow([order.id, order.user.username, order.status, order.created_at, order.updated_at])

        return response

    download_orders.short_description = 'Download selected orders as CSV'

