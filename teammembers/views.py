from rest_framework import generics
from teammembers.models import TeamMembers
from teammembers.serializer import TeamMembersSerializer


class TeamMembersList(generics.ListAPIView):
    serializer_class = TeamMembersSerializer
    queryset = TeamMembers.objects.get_queryset()