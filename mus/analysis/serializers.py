from rest_framework import serializers

from analysis.models import Analysis
from analysis.services.validators import validate_ids


class AnalysisSerializer(serializers.ModelSerializer):

    class Meta:
        model = Analysis
        fields = '__all__'

    def validate(self, data):
        validate_ids(data)
        return data