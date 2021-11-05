from rest_framework.permissions import BasePermission





# IsAdmin
# IsModerator
# IsUser

class IsAdmin(BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.role == request.user.role
