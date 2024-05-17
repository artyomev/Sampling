from rest_framework import routers

from analysis.views import AnalysisViewSet, AnalysisParametersViewSet

router = routers.SimpleRouter()
router.register(r'analysis', AnalysisViewSet)
router.register(r'analysis_parameters', AnalysisParametersViewSet)