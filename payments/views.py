from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from accounts.models import User
from common.permissions import IsAdminRole, IsResidentOrAdmin

from .models import FeeInvoice, Payment
from .serializers import FeeInvoiceSerializer, PaymentSerializer


class FeeInvoiceViewSet(viewsets.ModelViewSet):
    queryset = FeeInvoice.objects.select_related('flat').all()
    serializer_class = FeeInvoiceSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAuthenticated(), IsAdminRole()]
        return [IsAuthenticated(), IsResidentOrAdmin()]

    def get_queryset(self):
        user = self.request.user
        if user.role == User.Role.ADMIN:
            return super().get_queryset()
        return FeeInvoice.objects.filter(flat__resident=user)


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.select_related('invoice', 'paid_by').all()
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated, IsResidentOrAdmin]

    def get_queryset(self):
        user = self.request.user
        if user.role == User.Role.ADMIN:
            return super().get_queryset()
        return Payment.objects.filter(paid_by=user)

    def perform_create(self, serializer):
        payment = serializer.save(paid_by=self.request.user)
        invoice = payment.invoice
        if payment.amount >= invoice.amount + invoice.penalty_amount:
            invoice.is_paid = True
            invoice.save(update_fields=['is_paid'])
