from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    """Доступ администратору или только чтение"""

    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS
