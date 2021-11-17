from rest_framework import permissions
from rest_framework.permissions import BasePermission


class IsAdminOrReadOnly(permissions.BasePermission):
    """Доступ администратору или только чтение"""

    def has_permission(self, request, view):
        return (request.method in permissions.SAFE_METHODS
                or (request.user.is_authenticated
                    and request.user.is_admin))


class IsAdmin(BasePermission):

    def has_permission(self, request, view):
        return request.user.is_admin or request.user.is_staff


class IsAuthorOrModerOrAdmin(BasePermission):

    def has_object_permission(self, request, view, obj):
        return (
            obj.author == request.user
            or request.user.is_admin
            or request.user.is_moderator
            or request.user.is_staff
        )
