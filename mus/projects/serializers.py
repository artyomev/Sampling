from rest_framework import serializers
from musauth.serializers import MusUserSerializer

from projects.models import Project, ProjectTeam


class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'



class ProjectTeamSerializer(serializers.ModelSerializer):
    partner = MusUserSerializer()
    manager = MusUserSerializer()
    incharge = MusUserSerializer()
    staff = MusUserSerializer(many = True)

    class Meta:
        model = ProjectTeam
        fields = ['project', 'manager', 'partner', 'incharge', 'staff']

