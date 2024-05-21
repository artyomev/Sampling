from django.http import FileResponse
from django.shortcuts import render

from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import InitialUploadedFile
from .serializers import InitialFileSerializer


class FileUploadAPIView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    serializer_class = InitialFileSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            # you can access the file like this from serializer
            # uploaded_file = serializer.validated_data["file"]
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

