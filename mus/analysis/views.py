import os

from django.http import FileResponse
from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import  Response
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.viewsets import ModelViewSet

from analysis.models import Analysis, AnalysisParameters
from analysis.serializers import AnalysisSerializer, AnalysisParametersSerializer, ExecuteAnalysisSerializer
from analysis.services.main_analysis import process_files
from importfiles.models import project_files_folder
from importfiles.storage import uploads_storage


class AnalysisViewSet(ModelViewSet):
    queryset = Analysis.objects.all()
    serializer_class = AnalysisSerializer

class AnalysisParametersViewSet(ModelViewSet):
    queryset = AnalysisParameters.objects.all()
    serializer_class = AnalysisParametersSerializer


class ExecuteAnalysis(GenericAPIView):

    parser_classes = (MultiPartParser, FormParser)
    serializer_class = ExecuteAnalysisSerializer
    def get(self, request, *args, **kwargs):
        # try:
        pk = kwargs.get('pk', 0)
        obj = Analysis.objects.get(id=pk)
        analysis_name = obj.analysis_name
        spm = obj.analysisparameters.spm
        files = obj.files.all()
        new_sample_path_save = os.path.join(uploads_storage.location,
                                project_files_folder(files.first(), ""),
                                "done", analysis_name+".csv")
        print(new_sample_path_save)
        process_files(files, spm, new_sample_path_save)
        response = FileResponse(open(new_sample_path_save, 'rb'))
        return response
        # except Exception as e:
        #     return Response(
        #         repr(e),
        #         status=status.HTTP_400_BAD_REQUEST
        #     )

    def get_queryset(self):
        pass