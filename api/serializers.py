from rest_framework import serializers
from api.models import Trail

class TrailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trail
        fields = ('id', 'name', 'latitude', 'longitude', 'length', 'difficulty', 'restroom')
