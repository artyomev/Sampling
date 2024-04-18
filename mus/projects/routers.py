from rest_framework import routers

from projects.views import ProjectViewSet, ProjectTeamViewSet

router = routers.SimpleRouter()
router.register(r'projects', ProjectViewSet)
router.register(r'teams', ProjectTeamViewSet, basename='project_teams')
# router.register(r'userprojects', ProjectByUserViewSet, basename='userprojects')