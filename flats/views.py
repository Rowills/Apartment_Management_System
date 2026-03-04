from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from accounts.models import User
from common.permissions import IsAdminRole, IsResidentOrAdmin

from .models import Flat
from .serializers import FlatSerializer


class FlatViewSet(viewsets.ModelViewSet):
    queryset = Flat.objects.select_related('owner', 'resident').all()
    serializer_class = FlatSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [IsAuthenticated(), IsResidentOrAdmin()]
        return [IsAuthenticated(), IsAdminRole()]

    def get_queryset(self):
        user = self.request.user
        if user.role == User.Role.ADMIN:
            return super().get_queryset()
        return Flat.objects.filter(resident=user)
