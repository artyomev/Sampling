from rest_framework import serializers


def validate_ids(data):
    try:
        for file in data['files']:
            if file.project != data['project']:
                raise serializers.ValidationError('Selected files belong to another project!')
    except Exception as e:
        raise serializers.ValidationError(e)

def validate_randomseed(data):
    try:
        if data['generate_random_seed'] == False:
            if data['random_seed'] < 1000000:
                raise serializers.ValidationError('Bad random seed!')
    except Exception as e:
        raise serializers.ValidationError(e)