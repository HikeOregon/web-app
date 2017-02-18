from rest_framework import serializers
from rest_framework.utils.serializer_helpers import ReturnDict
from api.models import Trail


class TrailListSerializer(serializers.ListSerializer):
    class Meta:
        model = Trail
        fields = ('id', 'name', 'latitude', 'longitude', 'length', 'difficulty', 'restroom')

    @property
    def data(self):
        ret = super(serializers.ListSerializer, self).data
        ret = {'trails': ret}
        return ReturnDict(ret, serializer=self)

class TrailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trail
        fields = ('id', 'name', 'latitude', 'longitude', 'length', 'difficulty', 'restroom')
        list_serializer_class = TrailListSerializer
