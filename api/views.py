from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.filters import SearchFilter
from api.models import Trail
from api.serializers import TrailSerializer

class TrailViewSet(viewsets.ModelViewSet):
    """
    This is the API endpoint for lists of trails and individual trail details.
    You can use the **Filters** button in the top-right to use the search feature.

    ## A Single Trail

    Get individual trails by the `pk` parameter.  For example, to get the trail
    with `pk=1`, use:

        /api/trails/?pk=1


    ## Name Search

    To search for trails by name use the `search` parameter.  For example,
    searching for a trail with the word *Lake* in the name:

        /api/trails/?search=Lake




    """
    queryset = Trail.objects.all()
    serializer_class = TrailSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = (SearchFilter,)
    search_fields = ('name',)
