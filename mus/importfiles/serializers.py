from rest_framework import serializers

from importfiles.models import InitialUploadedFile
from importfiles.services.validators import validate_extension


class InitialFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = InitialUploadedFile
        fields = '__all__'

    def validate_initial_file(self, data):
        validate_extension(data.file_name)
