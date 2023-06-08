from django.contrib import admin
from .models import Notification
from django.http import HttpResponse
import csv

class NotificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'message', 'timestamp', 'is_read')
    actions = ['download_csv']

    def download_csv(self, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="notifications.csv"'

        writer = csv.writer(response)
        writer.writerow(['User', 'Message', 'Timestamp', 'Is Read'])

        for notification in queryset:
            writer.writerow([notification.user, notification.message, notification.timestamp, notification.is_read])

        return response

    download_csv.short_description = "Download selected notifications as CSV"

admin.site.register(Notification, NotificationAdmin)
