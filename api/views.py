"""views.py

Copyright © 2017 HikeOregon. All rights reserved.
Created by Bobby Eshleman on 2/18/2017.

"""


from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.filters import SearchFilter, DjangoFilterBackend
from api.models import Trail, TrailImage
from api.serializers import TrailSerializer, TrailImageSerializer


class TrailViewSet(viewsets.ModelViewSet):
    queryset = Trail.objects.all()
    serializer_class = TrailSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = (SearchFilter, DjangoFilterBackend,)
    search_fields = ('name',)
    filter_fields = ('difficulty', 'restroom', 'length',)

    def retrieve(self, request, pk=None):
        queryset = Trail.objects.all()
        trail = get_object_or_404(queryset, pk=pk)
        # To keep the retrieve and list API's uniform, we pass in the single trail as a list
        # and set `many` to True
        serializer = TrailSerializer([trail], many=True)
        return Response(serializer.data)


class TrailImageViewSet(viewsets.ModelViewSet):
    queryset = TrailImage.objects.all()
    serializer_class = TrailImageSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('trail',)
