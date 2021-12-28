from .base import BaseSerializer
from ..models.news import News


class NewsSerializer(BaseSerializer):
    class Meta:
        model = News
        fields = ("date", "subject", "content")
