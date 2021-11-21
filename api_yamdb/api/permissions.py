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


class ReviewPermissions(BasePermission):

    def has_object_permission(self, request, view, obj):

        if request.user.is_authenticated:

            if request.method in ('POST',):
                return True

            if request.method in ('PATCH', 'DELETE',) and (
                obj.author == request.user
                or request.user.is_admin
                or request.user.is_moderator
                or request.user.is_staff
            ):
                return True



        if request.method in ('GET'):
            return True







    # def has_object_permission(self, request, view, obj):
    #     if request.method in ('create',) and request.user.is_authenticated:
    #         return True
    #     elif request.method in ('list', 'retrieve'):
    #         return True
    #     elif (request.method in ('update', 'partial_update', 'destroy',)
    #         and (
    #             obj.author == request.user
    #             or request.user.is_admin
    #             or request.user.is_moderator
    #             or request.user.is_staff
    #         )):
    #             return True
    #     else:
    #         return (
    #             request.user.is_authenticated
    #             and (obj.author == request.user
    #             or request.user.is_admin
    #             or request.user.is_moderator
    #             or request.user.is_staff)
    #         )
