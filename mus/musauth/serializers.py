from musauth.models import MusUser
from rest_framework import serializers

class MusUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = MusUser
        fields = ['id', 'username', 'first_name', 'last_name', 'email']