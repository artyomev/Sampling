from rest_framework import serializers


def validate_ids(data):
    print(data)
    try:
        for file in data['files']:
            if file.project != data['project']:
                raise serializers.ValidationError('Selected files belong to another project!')
    except Exception as e:
        raise serializers.ValidationError(e)
