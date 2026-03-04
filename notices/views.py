from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from common.permissions import IsAssociationStaffOrAdmin

from .models import Notice
from .serializers import NoticeSerializer


class NoticeViewSet(viewsets.ModelViewSet):
    queryset = Notice.objects.select_related('published_by').all()
    serializer_class = NoticeSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [IsAuthenticated()]
        return [IsAuthenticated(), IsAssociationStaffOrAdmin()]

    def perform_create(self, serializer):
        serializer.save(published_by=self.request.user)
