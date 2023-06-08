from django.contrib import admin
from .models import PaymentMethod, Payment, Transaction
import csv
from django.http import HttpResponse

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount', 'payment_method', 'timestamp')
    actions = ['download_payments_as_csv']

    def download_payments_as_csv(self, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="payments.csv"'

        writer = csv.writer(response)
        writer.writerow(['User', 'Amount', 'Payment Method', 'Timestamp'])

        for payment in queryset:
            writer.writerow([payment.user, payment.amount, payment.payment_method, payment.timestamp])

        return response

    download_payments_as_csv.short_description = "Download selected payments as CSV"

admin.site.register(PaymentMethod)
admin.site.register(Payment, PaymentAdmin)
admin.site.register(Transaction)
