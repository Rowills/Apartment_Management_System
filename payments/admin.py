from django.contrib import admin

from .models import FeeInvoice, Payment


@admin.register(FeeInvoice)
class FeeInvoiceAdmin(admin.ModelAdmin):
    list_display = ('flat', 'month', 'amount', 'due_date', 'penalty_amount', 'is_paid')


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('receipt_number', 'invoice', 'amount', 'method', 'paid_by', 'paid_at')
