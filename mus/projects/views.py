from django.views.generic import DetailView, ListView
from rest_framework import viewsets, mixins
from rest_framework.decorators import action

from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser

from importfiles.serializers import InitialFileSerializer
from musauth.models import MusUser
from musauth.serializers import MusUserSerializer
from projects.models import Project
from projects.serializers import ProjectsSerializer, ProjectTeamSerializer


class ProjectViewSet(viewsets.ReadOnlyModelViewSet):
    """Возвращает список всех созданных проектов"""
    queryset = Project.objects.all()
    serializer_class = ProjectsSerializer
    permission_classes = (IsAdminUser,)


class ProjectTeamViewSet(mixins.RetrieveModelMixin,
                           GenericViewSet):
    """Возвращает список простой команды про проекту"""
    @action(detail=True, methods=['get'])
    def get_team(self, request, pk=None):
        users= Project.objects.get(id=pk).users.all()
        return Response({'project_id': pk, 'team': [{'id': u.id, 'login': u.username} for u in users]})

    """Возвращает детализированный список команды по проекту"""
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


class UserProjectViewSet(mixins.RetrieveModelMixin,
                           GenericViewSet):
    """Возвращает список проектов конкретного пользователя"""

    @action(detail=True, methods=['get'])
    def get_user_projects(self, request, pk=None):
        user = MusUser.objects.filter(id=pk).first()
        return Response({'user_id': pk,
                         'projects' : [ProjectsSerializer(p).data for p in user.project_set.all()]
                         })

class ProjectFilesViewSet(mixins.RetrieveModelMixin,
                           GenericViewSet):
    @action(detail=True, methods=['get'])
    def get_project_files(self, request, pk=None):
        project = Project.objects.filter(id=pk).first()
        return Response({'project_id': pk,
                         'files': [InitialFileSerializer(p).data for p in project.initialuploadedfile_set.all()]
                         })

class ProjectDetail(DetailView):
    model = Project


class ProjectList(ListView):
    model = Project