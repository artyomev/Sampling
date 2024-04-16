from django.db.models import Subquery, Q
from django.shortcuts import render
from rest_framework import generics, viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from django.core.serializers import serialize
from rest_framework.viewsets import GenericViewSet

from musauth.models import MusUser
from projects.models import Project, ProjectTeam
from projects.serializers import ProjectsSerializer, ProjectTeamSerializer


class ProjectViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectsSerializer

class ProjectTeamViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ProjectTeam.objects.all()
    serializer_class = ProjectTeamSerializer


class ProjectByUserViewSet(mixins.RetrieveModelMixin,
                           GenericViewSet):

    @action(detail=True, methods=['get'])
    def get_user_projects_detail(self, request, pk=None):

        user = MusUser.objects.get(id=pk)
        projectteams_as_staff = user.staff_of.all()
        projectteams_as_manager = user.manager.all()
        projectteams_as_partner = user.partner.all()
        projectteams_as_incharge = user.incharge.all()

        resp = {}
        resp['user'] = user.username
        resp['project as manager'] = [ProjectsSerializer(p.project).data['title'] for p in projectteams_as_manager]
        resp['project as staff'] = [ProjectsSerializer(p.project).data['title']for p in projectteams_as_staff]
        resp['project as partner'] = [ProjectsSerializer(p.project).data['title'] for p in projectteams_as_partner]
        resp['project as incharge'] = [ProjectsSerializer(p.project).data['title'] for p in projectteams_as_incharge]
        return Response(resp)

    @action(detail=True, methods=['get'])
    def get_user_projects(self, request, pk=None):
        user = MusUser.objects.get(id=pk)
        projectteams_as_staff = user.staff_of.all()
        projectteams_as_manager = user.manager.all()
        projectteams_as_partner = user.partner.all()
        projectteams_as_incharge = user.incharge.all()

        resp = {}
        projects_list = []
        projects_list.extend([ProjectsSerializer(p.project).data['title']
                                            for p in projectteams_as_partner])
        projects_list.extend([ProjectsSerializer(p.project).data['title']
                                              for p in projectteams_as_manager])
        projects_list.extend([ProjectsSerializer(p.project).data['title']
                                              for p in projectteams_as_incharge])
        projects_list.extend([ProjectsSerializer(p.project).data['title']
                                              for p in projectteams_as_staff])
        resp['user'] = user.username
        resp['projects'] = projects_list
        return Response(resp)
