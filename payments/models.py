from django.conf import settings
from django.db import models

from flats.models import Flat


class FeeInvoice(models.Model):
    flat = models.ForeignKey(Flat, on_delete=models.CASCADE, related_name='fee_invoices')
    month = models.DateField(help_text='Use first day of month.')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    due_date = models.DateField()
    penalty_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    is_paid = models.BooleanField(default=False)

    class Meta:
        unique_together = ('flat', 'month')
        ordering = ['-month']

    def __str__(self):
        return f'{self.flat} - {self.month:%Y-%m}'


class Payment(models.Model):
    class Method(models.TextChoices):
        ONLINE = 'online', 'Online'
        CASH = 'cash', 'Cash'
        BANK_TRANSFER = 'bank_transfer', 'Bank Transfer'

    invoice = models.ForeignKey(FeeInvoice, on_delete=models.CASCADE, related_name='payments')
    paid_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    method = models.CharField(max_length=20, choices=Method.choices, default=Method.ONLINE)
    gateway_transaction_id = models.CharField(max_length=120, blank=True)
    receipt_number = models.CharField(max_length=50, unique=True)
    paid_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-paid_at']

    def __str__(self):
        return self.receipt_number
