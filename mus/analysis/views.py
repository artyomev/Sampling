from rest_framework.viewsets import ModelViewSet

from analysis.models import Analysis
from analysis.serializers import AnalysisSerializer


class AnalysisViewSet(ModelViewSet):
    queryset = Analysis.objects.all()
    serializer_class = AnalysisSerializer




