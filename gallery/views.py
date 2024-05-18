from rest_framework import generics
from gallery.models import Gallery
from gallery.serializer import GallerySerializer


class GalleryList(generics.ListAPIView):
    serializer_class = GallerySerializer 
    queryset = Gallery.objects.get_queryset()