from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from api.models import Trail
from api.serializers import TrailSerializer

class TrailViewSet(viewsets.ModelViewSet):
    """
    A simple viewset for viewing Trails.
    """
    queryset = Trail.objects.all()
    serializer_class = TrailSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
