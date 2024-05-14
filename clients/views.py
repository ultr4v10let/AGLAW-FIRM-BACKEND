from rest_framework import generics
from clients.models import Clients
from clients.serializer import ClientsSerializer


class ClinetsList(generics.ListAPIView):
    serializer_class = ClientsSerializer
    queryset = Clients.objects.get_queryset()