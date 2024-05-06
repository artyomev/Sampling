from rest_framework import serializers

from musauth.models import MusUser
from projects.models import Project


class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'title']



class ProjectTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = MusUser
        fields = '__all__'

