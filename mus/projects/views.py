
from rest_framework import viewsets, mixins
from rest_framework.decorators import action

from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response

from musauth.serializers import MusUserSerializer
from projects.models import Project
from projects.serializers import ProjectsSerializer, ProjectTeamSerializer


class ProjectViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectsSerializer


class ProjectTeamViewSet(mixins.RetrieveModelMixin,
                           GenericViewSet):
    @action(detail=True, methods=['get'])
    def get_team(self, request, pk=None):
        users= Project.objects.get(id=pk).users.all()
        return Response({'project_id': pk, 'team': [{'id': u.id, 'login': u.username} for u in users]})

    @action(detail=True, methods=['get'])
    def get_team_detailed(self, request, pk=None):
        users = Project.objects.get(id=pk).users.all()
        return Response(
            {'project_id': pk,
             'partner': MusUserSerializer(users.filter(projectteamrole__role='Partner').first()).data,
             'manager': MusUserSerializer(users.filter(projectteamrole__role='Manager').first()).data,
             'incharge': MusUserSerializer(users.filter(projectteamrole__role='Incharge').first()).data,
             'staff': [MusUserSerializer(u).data for u in users.filter(projectteamrole__role='Staff')]
             }
        )


