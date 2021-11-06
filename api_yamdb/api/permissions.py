from rest_framework import permissions
from rest_framework.permissions import BasePermission


class IsAdminOrReadOnly(permissions.BasePermission):
    """Доступ администратору или только чтение"""

    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS






# IsAdmin
# IsModerator
# IsUser

class IsAdmin(BasePermission):

    def has_object_permission(self, request, view, obj):
        return True
