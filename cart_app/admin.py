from django.contrib import admin
from django.http import HttpResponse
import csv
from openpyxl import Workbook

from .models import Cart, CartItem


class CartItemInline(admin.TabularInline):
    model = CartItem


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'created_at')
    inlines = [CartItemInline]

    actions = ['export_to_csv', 'export_to_excel']

    def export_to_csv(self, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="cart_data.csv"'
        writer = csv.writer(response)
        writer.writerow(['Cart ID', 'User', 'Created At'])

        for cart in queryset:
            writer.writerow([cart.id, cart.user.username, cart.created_at])

        return response

    def export_to_excel(self, request, queryset):
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename="cart_data.xlsx"'
        workbook = Workbook()
        worksheet = workbook.active
        worksheet.title = 'Cart Data'
        worksheet.append(['Cart ID', 'User', 'Created At'])

        for cart in queryset:
            worksheet.append([cart.id, cart.user.username, cart.created_at])

        workbook.save(response)
        return response

    export_to_csv.short_description = 'Export selected carts to CSV'
    export_to_excel.short_description = 'Export selected carts to Excel'


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'cart', 'product', 'quantity')
