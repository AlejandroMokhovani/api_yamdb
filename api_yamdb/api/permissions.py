from rest_framework.permissions import BasePermission





# IsAdmin
# IsModerator
# IsUser

class IsAdmin(BasePermission):

    def has_permission(self, request, view):
        return request.user.role == 'admin' or request.user.is_staff

    # def has_object_permission(self, request, view, obj):
    #     return request.user.role == 'admin' or request.user.is_staff
