from rest_framework import serializers

from importfiles.services.parsers import get_extension


def validate_extension(data):
    allowed_extensions = ['xlsx', 'xls', 'xlsm', 'xlsb', 'csv', 'txt']
    try:
        file_name = data.name
        ext = get_extension(file_name)
        if ext not in allowed_extensions:
            raise serializers.ValidationError('Wrong extension!')
    except Exception as e:
        raise serializers.ValidationError(e)

