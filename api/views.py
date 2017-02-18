from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.filters import SearchFilter
from api.models import Trail
from api.serializers import TrailSerializer

class TrailViewSet(viewsets.ModelViewSet):
    """
    A simple viewset for viewing Trails.
    """
    queryset = Trail.objects.all()
    serializer_class = TrailSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = (SearchFilter,)
    search_fields = ('name',)
