from rest_framework import serializers


def validate_extension(data):
    allowed_extensions = ['xlsx', 'xls', 'xlsm', 'xlsb', 'csv', 'txt']
    try:
        file_name = data.name
        ext = file_name.split('.')[-1]
        if ext not in allowed_extensions:
            raise serializers.ValidationError('Wrong extension!')
    except Exception as e:
        raise serializers.ValidationError(e)

