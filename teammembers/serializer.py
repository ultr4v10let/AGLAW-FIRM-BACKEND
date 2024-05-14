
from rest_framework import serializers
from teammembers.models import TeamMembers

class TeamMembersSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMembers
        fields = '__all__'