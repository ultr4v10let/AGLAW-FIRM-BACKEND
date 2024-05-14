from rest_framework import generics
from news.models import News
from news.serializer import NewsSerializer


class NewsList(generics.ListAPIView):
    serializer_class = NewsSerializer 
    queryset = News.objects.get_queryset()