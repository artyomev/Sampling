from rest_framework import serializers


def validate_extension(file_name: str) -> None:
    allowed_extensions = ['xlsx', 'xls', 'xlsm', 'xlsb', 'csv', 'txt']
    try:
        ext = file_name.split('.')[-1]
        if ext not in allowed_extensions:
            raise serializers.ValidationError('Wrong extension!')
    except Exception as e:
        raise serializers.ValidationError(e)

