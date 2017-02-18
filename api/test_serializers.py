"""test_models.py

Copyright © 2017 HikeOregon. All rights reserved.
Created by Bobby Eshleman on 2/18/2017.

"""


from django.test import TestCase
from rest_framework import serializers
from api.models import Trail
from api.serializers import TrailSerializer


class TrailSerializerTestCase(TestCase):
    
    fields = dict(
            name='Multnomah Falls',
            latitude=12.32,
            longitude=13.11,
            length=20.1,
            difficulty=4,
            restroom=True,
    )

    def test_okay(self):
        trail = Trail.objects.create(**self.fields)
        serializer = TrailSerializer([trail], many=True)
        fields = self.fields.copy()
        fields['id'] = 1
        fields = {'trails': [fields]}
        self.assertDictEqual(serializer.data, fields)

    def test_latitude_min(self):
        fields = self.fields.copy()
        fields['latitude'] = -300
        serializer = TrailSerializer(data=fields)
        with self.assertRaises(serializers.ValidationError):
            serializer.is_valid(raise_exception=True)

    def test_latitude_max(self):
        fields = self.fields.copy()
        fields['latitude'] = 300
        serializer = TrailSerializer(data=fields)
        with self.assertRaises(serializers.ValidationError):
            serializer.is_valid(raise_exception=True)

    def test_longitude_min(self):
        fields = self.fields.copy()
        fields['latitude'] = -300
        serializer = TrailSerializer(data=fields)
        with self.assertRaises(serializers.ValidationError):
            serializer.is_valid(raise_exception=True)

    def test_longitude_max(self):
        fields = self.fields.copy()
        fields['longitude'] = 300
        serializer = TrailSerializer(data=fields)
        with self.assertRaises(serializers.ValidationError):
            serializer.is_valid(raise_exception=True)
