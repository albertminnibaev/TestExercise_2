from rest_framework.permissions import BasePermission


# пользователь является автором
class IsAuthor(BasePermission):
    message = "Вы не являетесь автором, у вас нет права доступа,"

    def has_object_permission(self, request, view, obj):
        return request.user == obj.author


# Проверка на то, что нользователь является администратором
class IsAdmin(BasePermission):
    message = 'Вы не являетесь администратром'

    def has_permission(self, request, view):
        return request.user.is_admin
