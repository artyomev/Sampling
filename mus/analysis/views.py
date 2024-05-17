from rest_framework.viewsets import ModelViewSet

from analysis.models import Analysis, AnalysisParameters
from analysis.serializers import AnalysisSerializer, AnalysisParametersSerializer


class AnalysisViewSet(ModelViewSet):
    queryset = Analysis.objects.all()
    serializer_class = AnalysisSerializer

class AnalysisParametersViewSet(ModelViewSet):
    queryset = AnalysisParameters.objects.all()
    serializer_class = AnalysisParametersSerializer




