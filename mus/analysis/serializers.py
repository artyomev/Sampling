from rest_framework import serializers

from analysis.models import Analysis, AnalysisParameters
from analysis.services.validators import validate_ids, validate_randomseed


class AnalysisSerializer(serializers.ModelSerializer):

    class Meta:
        model = Analysis
        fields = '__all__'

    def validate(self, data):
        validate_ids(data)
        return data

class AnalysisParametersSerializer(serializers.ModelSerializer):

    class Meta:
        model = AnalysisParameters
        fields = '__all__'

        def validate(self, data):
            validate_randomseed(data)
            return data
