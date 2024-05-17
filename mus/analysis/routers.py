from rest_framework import routers

from analysis.views import AnalysisViewSet

router = routers.SimpleRouter()
router.register(r'analysis', AnalysisViewSet)