from rest_framework import serializers

from importfiles.models import InitialUploadedFile
from importfiles.services.validators import validate_extension, validate_delimiter_presence
from importfiles.services.validators import validate_decimal_separator_presence, validate_thousand_separator_presence


class InitialFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = InitialUploadedFile
        fields = '__all__'

    def validate_initial_file(self, file):
        validate_extension(file)
        return file

    def validate(self, data):
        validate_delimiter_presence(data)
        validate_thousand_separator_presence(data)
        validate_decimal_separator_presence(data)
        return data

