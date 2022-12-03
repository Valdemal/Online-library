from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsStaffOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True

        return bool(request.user and request.user.is_staff)

class IsAuthor(BasePermission):
    """
    Если пользователь является автором, то он имеет право совершать любые действия со своим объектом.
    """

    def has_object_permission(self, request, view, obj):
        print(request.user)
        return bool(request.user and obj.user == request.user)

    def has_permission(self, request, view):
        return request.method in SAFE_METHODS

class CanCreateIfAuthenticated(BasePermission):
    """
    Если пользователь зарегистрирован, то он может создать объект
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.method == 'POST')

    def has_object_permission(self, request, view, obj):
        return False
