from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.core.serializers import serialize

from projects.models import Project, ProjectTeam
from projects.serializers import ProjectsSerializer, ProjectTeamSerializer


class ProjectViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectsSerializer

class ProjectTeamViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ProjectTeam.objects.all()
    serializer_class = ProjectTeamSerializer
