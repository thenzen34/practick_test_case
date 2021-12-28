from rest_framework import viewsets

from news.models import News
from news.serializers.news import NewsSerializer


class NewsViewSet(viewsets.ModelViewSet):
    serializer_class = NewsSerializer
    queryset = News.objects.all()
