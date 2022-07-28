from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """Проверка метода запроса и статуса пользователя.

    Полный доступ к объекту только для владельцев объекта.
    """
    message = 'Данное действие разрешено только автору!'

    def has_permission(self, request, view):
        return (request.method in permissions.SAFE_METHODS
                or request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        return obj.author == request.user


class ReadOnly(permissions.BasePermission):
    """Доступ к просмотру конкретного объекта."""

    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS
