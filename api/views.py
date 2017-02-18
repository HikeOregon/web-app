"""views.py

Copyright © 2017 HikeOregon. All rights reserved.
Created by Bobby Eshleman on 2/18/2017.

"""


from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.filters import SearchFilter, DjangoFilterBackend
from api.models import Trail
from api.serializers import TrailSerializer


class TrailViewSet(viewsets.ModelViewSet):
    """
    This is the API endpoint for lists of trails and individual trail details.
    You can use the **Filters** button in the top-right to use the search feature.

    ## A Single Trail

    Get individual trails by using their `id`.  For example, to get the trail
    with `id=1`, use:

        /api/trails/1


    ## Name Search

    To search for trails by name use the `search` parameter.  For example,
    searching for a trail with the word *Lake* in the name:

        /api/trails/?search=Lake

    ## Query Parameter Filtering

    To get all trails with a difficulty of 4:

        /api/trails/?difficulty=4

    To get all trails with a difficulty of 4 and that have a restroom:

        /api/trails/?difficulty=4&restroom=true


    """

    queryset = Trail.objects.all()
    serializer_class = TrailSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = (SearchFilter, DjangoFilterBackend,)
    search_fields = ('name',)
    filter_fields = ('difficulty', 'restroom', 'length',)

    def retrieve(self, request, pk=None):
        """Returns a list Response containing only one result.

        The return format is the same as the list view.  This is done for API uniformity.

        """
        queryset = Trail.objects.all()
        trail = get_object_or_404(queryset, pk=pk)
        # To keep the retrieve and list API's uniform, we pass in the single trail as a list
        # and set `many` to True
        serializer = TrailSerializer([trail], many=True)
        return Response(serializer.data)
