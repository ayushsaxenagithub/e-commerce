from django.contrib import admin
from .models import Wishlist

class WishlistAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'added_at')
    list_filter = ('user', 'added_at')
    search_fields = ('user__username', 'product__title')
    actions = ['download_selected_as_excel']

    def download_selected_as_excel(self, request, queryset):
        # Logic to download selected items as Excel
        pass

    download_selected_as_excel.short_description = 'Download selected as Excel'

admin.site.register(Wishlist, WishlistAdmin)
