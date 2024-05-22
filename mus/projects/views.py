from django.views.generic import DetailView, ListView

from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, mixins, status
from rest_framework.decorators import action, api_view

from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser

from importfiles.serializers import InitialFileSerializer
from musauth.models import MusUser
from musauth.serializers import MusUserSerializer
from projects.models import Project
from projects.serializers import ProjectsSerializer, ProjectTeamSerializer
from projects.uils import team_response_schema_dict, team_detailed_response_schema_dict, \
    userprojects_response_schema_dict


class ProjectViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectsSerializer
    permission_classes = (IsAdminUser,)


class ProjectTeamViewSet(GenericViewSet):
    # retriver override
    serializer_class = ProjectsSerializer

    def get_queryset(self):
        pass

    @swagger_auto_schema(method='get', responses=team_response_schema_dict)
    @action(detail=True, methods=['get'])
    def get_team(self, request, pk=None):
        """Возвращает простой список команды про проекту"""
        users= Project.objects.get(id=pk).users.all()
        return Response({'project_id': pk, 'team': [{'id': u.id, 'login': u.username} for u in users]})

    @swagger_auto_schema(method='get', responses=team_detailed_response_schema_dict)
    @action(detail=True, methods=['get'])
    def get_team_detailed(self, request, pk=None):
        """Возвращает детализированный список команды по проекту"""

        try:
            users = Project.objects.get(id=pk).users.all()
            return Response(
                {'project_id': pk,
                 'partner': MusUserSerializer(users.filter(projectteamrole__role='Partner').first()).data,
                 'manager': MusUserSerializer(users.filter(projectteamrole__role='Manager').first()).data,
                 'incharge': MusUserSerializer(users.filter(projectteamrole__role='Incharge').first()).data,
                 'staff': [MusUserSerializer(u).data for u in users.filter(projectteamrole__role='Staff')]
                 }

            )
        except Exception as e:
            return Response(
                repr(e),
                status=status.HTTP_400_BAD_REQUEST)


class UserProjectViewSet(GenericViewSet):
    serializer_class = ProjectsSerializer
    """Возвращает список проектов конкретного пользователя"""

    def get_queryset(self):
        pass

    @swagger_auto_schema(responses=userprojects_response_schema_dict)
    @action(detail=True, methods=['get'])
    def get_user_projects(self, request, pk=None):

        try:
            user = MusUser.objects.filter(id=pk).first()
            return Response({'user_id': pk,
                         'projects' : [ProjectsSerializer(p).data for p in user.project_set.all()]
                         })
        except Exception as e:
            return Response(
                repr(e),
                status=status.HTTP_400_BAD_REQUEST)

class ProjectFilesViewSet(GenericViewSet):
    serializer_class = InitialFileSerializer

    def get_queryset(self):
        pass
    @action(detail=True, methods=['get'])
    def get_project_files(self, request, pk=None):

        try:
            project = Project.objects.filter(id=pk).first()
            return Response({'project_id': pk,
                             'files': [InitialFileSerializer(p).data for p in project.initialuploadedfile_set.all()]
                             })
        except Exception as e:
            return Response(
                repr(e),
                status=status.HTTP_400_BAD_REQUEST)

class ProjectDetail(DetailView):
    model = Project


class ProjectList(ListView):
    model = Project