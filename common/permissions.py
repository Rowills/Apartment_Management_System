from rest_framework.permissions import BasePermission


class HasAnyRole(BasePermission):
    allowed_roles = []

    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.role in self.allowed_roles


class IsAdminRole(HasAnyRole):
    allowed_roles = ['admin']


class IsAssociationStaffOrAdmin(HasAnyRole):
    allowed_roles = ['association_staff', 'admin']


class IsSecurityOrAdmin(HasAnyRole):
    allowed_roles = ['security', 'admin']


class IsResidentOrAdmin(HasAnyRole):
    allowed_roles = ['resident', 'admin']
