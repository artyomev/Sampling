from django.shortcuts import render
from rest_framework import viewsets

from musauth.models import MusUser
from musauth.serializers import MusUserSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """Возвращает список всех созданных проектов"""
    queryset = MusUser.objects.all()
    serializer_class = MusUserSerializer

