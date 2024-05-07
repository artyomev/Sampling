from rest_framework import routers

from projects.views import ProjectViewSet, ProjectTeamViewSet, UserProjectViewSet, ProjectFilesViewSet

router = routers.SimpleRouter()
router.register(r'projects', ProjectViewSet)
router.register(r'teams', ProjectTeamViewSet, basename='project_teams')
router.register(r'userprojects', UserProjectViewSet, basename='userprojects')
router.register(r'project_files',ProjectFilesViewSet, basename='project_files')