from rest_framework import permissions


class IsProfileOwner(permissions.BasePermission):
    """
    Only allow owners of an object to edit it
    """

    def has_object_permission(self, request, view, obj):
        return request.user == obj.user
