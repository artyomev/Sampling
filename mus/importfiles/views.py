
from django.http import FileResponse
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from rest_framework import status

from rest_framework.generics import GenericAPIView
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import InitialUploadedFile
from .serializers import InitialFileSerializer, SingleDownloadSerializer, InitialFileUploadSerializer


class FileUploadAPIView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    serializer_class = InitialFileSerializer

    user_response = openapi.Response('After upload response', InitialFileSerializer)

    # https://drf-yasg.readthedocs.io/en/stable/custom_spec.html
    @swagger_auto_schema(request_body=InitialFileUploadSerializer, responses={201: user_response})
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class SingleDownloadFile(GenericAPIView):

    parser_classes = (MultiPartParser, FormParser)
    serializer_class = SingleDownloadSerializer

    def get(self, request, *args, **kwargs):
        try:
            pk = kwargs.get('pk', 0)
            obj = InitialUploadedFile.objects.get(id=pk)
            filename = obj.initial_file.path
            response = FileResponse(open(filename, 'rb'))
            return response
        except:
            return Response(
                'File with this ID could not be found!',
                status=status.HTTP_400_BAD_REQUEST
            )

    def get_queryset(self):
        pass