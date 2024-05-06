from rest_framework import permissions


class AddToTeamPermission(permissions.BasePermission):
    """Добавление в команду возможно только от уровня incharge и выше"""
    pass
