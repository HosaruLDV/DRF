from rest_framework.permissions import BasePermission


class OwnerPerms(BasePermission):

    def has_permission(self, request, view):
        if request.user == view.get_object().owner:
            return True
        else:
            return False


class ModerPerms(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_staff:
            return True
        else:
            return False
