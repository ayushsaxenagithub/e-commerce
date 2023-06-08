from django.contrib import admin
from django.http import HttpResponse
from .models import ProductSearch, UserSearch, OrderSearch, ReviewSearch


class SearchAdmin(admin.ModelAdmin):
    list_display = ['id']
    actions = ['download_search_data']

    def download_search_data(self, request, queryset):
        # Generate the CSV file content
        csv_data = "ID,Search Vector\n"
        for search_instance in queryset:
            csv_data += f"{search_instance.id},{search_instance.search_vector}\n"

        # Create the HTTP response with CSV file
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="search_data.csv"'
        response.write(csv_data)

        return response

    download_search_data.short_description = "Download selected search data"


admin.site.register(ProductSearch, SearchAdmin)
admin.site.register(UserSearch, SearchAdmin)
admin.site.register(OrderSearch, SearchAdmin)
admin.site.register(ReviewSearch, SearchAdmin)
