from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from accounts.models import User
from common.permissions import IsAssociationStaffOrAdmin, IsResidentOrAdmin

from .models import Ticket
from .serializers import TicketSerializer


class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.select_related('flat', 'raised_by', 'assigned_to').all()
    serializer_class = TicketSerializer

    def get_permissions(self):
        if self.action == 'create':
            return [IsAuthenticated(), IsResidentOrAdmin()]
        return [IsAuthenticated()]

    def get_queryset(self):
        user = self.request.user
        if user.role in [User.Role.ADMIN, User.Role.ASSOCIATION_STAFF]:
            return super().get_queryset()
        return Ticket.objects.filter(raised_by=user)

    def perform_create(self, serializer):
        serializer.save(raised_by=self.request.user)

    def perform_update(self, serializer):
        user = self.request.user
        if user.role in [User.Role.ASSOCIATION_STAFF, User.Role.ADMIN]:
            serializer.save()
        else:
            serializer.save(status=Ticket.Status.OPEN)
