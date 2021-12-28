
from rest_framework import serializers


class PingPongSerializer(serializers.Serializer):
    ping = serializers.CharField(
        allow_blank=True,
        default="",
        max_length=10,
        help_text="please input 'ping'"
    )

