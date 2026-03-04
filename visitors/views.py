from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from common.permissions import IsSecurityOrAdmin

from .models import VisitorLog
from .serializers import VisitorLogSerializer


class VisitorLogViewSet(viewsets.ModelViewSet):
    queryset = VisitorLog.objects.select_related('flat').all()
    serializer_class = VisitorLogSerializer
    permission_classes = [IsAuthenticated, IsSecurityOrAdmin]
