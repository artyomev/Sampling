from rest_framework import routers

from projects.views import ProjectViewSet, ProjectTeamViewSet, ProjectByUserViewSet

router = routers.SimpleRouter()
router.register(r'projects', ProjectViewSet)
router.register(r'projectsteams', ProjectTeamViewSet)
router.register(r'userprojects', ProjectByUserViewSet, basename='userprojects')