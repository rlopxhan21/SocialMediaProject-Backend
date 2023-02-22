from rest_framework import permissions

class CurrentUserOrAdminOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return obj.author.id == request.user.id or request.user.is_staff or request.user.is_superuser