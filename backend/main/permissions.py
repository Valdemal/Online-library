from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsStaffOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True

        return bool(request.user and request.user.is_staff)


class IsAuthorOrStaff(BasePermission):
    """
    Если пользователь является автором или персоналом, то он имеет право совершать любые действия с объектом.
    """

    def has_object_permission(self, request, view, obj):
        return bool(request.user) and (obj.user == request.user or request.user.is_staff)
