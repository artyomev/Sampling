from rest_framework import serializers

from importfiles.services.BaseParser import get_extension


def validate_extension(data):
    allowed_extensions = ['xlsx', 'xls', 'xlsm', 'xlsb', 'csv', 'txt']
    try:
        file_name = data.name
        ext = get_extension(file_name)
        if ext not in allowed_extensions:
            raise serializers.ValidationError('Wrong extension!')
    except Exception as e:
        raise serializers.ValidationError(e)


def validate_delimiter_presence(data):
    try:
        if get_extension(data['initial_file'].name) == 'txt':
            if data.get('txt_column_delimiter', "") == "":
                raise serializers.ValidationError('You have to determine column delimiter for text file!')
    except Exception as e:
        raise serializers.ValidationError(e)

def validate_decimal_separator_presence(data):
    try:
        if get_extension(data['initial_file'].name) in ('txt', 'csv'):
            if data.get('decimal_separator', "") == "":
                raise serializers.ValidationError('You have to determine decimal separator for text/csv file!')
    except Exception as e:
        raise serializers.ValidationError(e)

def validate_thousand_separator_presence(data):
    try:
        if get_extension(data['initial_file'].name) in ('txt', 'csv'):
            if data.get('thousand_separator', "") == "":
                raise serializers.ValidationError('You have to determine thousand separator for text/csv file!')
    except Exception as e:
        raise serializers.ValidationError(e)




