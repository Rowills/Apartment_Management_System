from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny

from common.permissions import IsAdminRole

from .models import User
from .serializers import UserSerializer


class UserViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action == 'create':
            return [AllowAny()]
        if self.action in ['list', 'update', 'partial_update']:
            return [IsAuthenticated(), IsAdminRole()]
        return [IsAuthenticated()]

    def get_queryset(self):
        user = self.request.user
        if user.role == User.Role.ADMIN:
            return super().get_queryset()
        return User.objects.filter(id=user.id)
