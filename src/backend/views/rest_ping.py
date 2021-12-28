
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from backend.serializer import PingPongSerializer


class PingPongViewSet(ViewSet):
    """
    dd
    """
    serializer_class = PingPongSerializer

    def get_serializer_context(self):
        return {
            'request': self.request,
            'format': self.format_kwarg,
            'view': self
        }

    def get_serializer(self, *args, **kwargs):
        kwargs['context'] = self.get_serializer_context()
        return self.serializer_class(*args, **kwargs)

    def create(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            if 'ping' == serializer.data['ping']:
                return Response({'result': 'pong'})
            else:
                return Response({'result': "What's in your head?"})
        else:
            return Response({'error': serializer.errors})

