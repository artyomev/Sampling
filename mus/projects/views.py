from django.shortcuts import render
from rest_framework import generics

from projects.models import Project
from projects.serializers import ProjectsSerializer


class ProjectsAPIView(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectsSerializer


class ProjectsUpdateAPIView(generics.UpdateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectsSerializer
