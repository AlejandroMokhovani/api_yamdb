from rest_framework import permissions
from rest_framework.permissions import BasePermission


class IsAdminOrReadOnly(permissions.BasePermission):
    """Доступ администратору или только чтение"""

    def has_permission(self, request, view):
        return (request.method in permissions.SAFE_METHODS
                or (request.user.is_authenticated
                    and request.user.is_admin))

    # def has_permission(self, request, view):
    #     if request.method in permissions.SAFE_METHODS:
    #         return True
    #     if request.user.is_authenticated:
    #         return bool(request.user.is_staff or request.user.role == 'admin')





# IsAdmin
# IsModerator
# IsUser

class IsAdmin(BasePermission):

    def has_object_permission(self, request, view, obj):
        return True
