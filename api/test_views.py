"""test_views.py

Copyright © 2017 HikeOregon. All rights reserved.
Created by Bobby Eshleman on 2/18/2017.

"""


from django.test import TestCase
from rest_framework.test import APIRequestFactory
from api.views import TrailViewSet
from api.models import Trail


class TrailViewSetTestCase(TestCase):

    def setUp(self):
        Trail.objects.create(
            name='Multnomah Falls',
            latitude=12.32,
            longitude=13.11,
            length=20.1,
            difficulty=4,
            restroom=True,
        )
        self.factory = APIRequestFactory()

    def test_detail(self):
        request = self.factory.get('/api/trails/1')
        detail_view = TrailViewSet.as_view({'get': 'retrieve'})
        response = detail_view(request, pk=1)
        response.render()
        first_item = response.data['trails'][0]
        self.assertEqual(first_item['name'], 'Multnomah Falls')

    def test_list(self):
        request = self.factory.get('/api/trails/')
        detail_view = TrailViewSet.as_view({'get': 'list'})
        response = detail_view(request)
        response.render()
        first_item = response.data['trails'][0]
        self.assertEqual(first_item['name'], 'Multnomah Falls')

    def test_filtering_difficulty(self):
        Trail.objects.create(
            name='Trilliam Lake',
            latitude=12.32,
            longitude=13.11,
            length=20.1,
            difficulty=4,
            restroom=True,
        )

        Trail.objects.create(
            name='Not Difficulty 4',
            latitude=12.32,
            longitude=13.11,
            length=20.1,
            difficulty=2,
            restroom=True,
        )

        request = self.factory.get('/api/trails/', {'difficulty': 4})
        detail_view = TrailViewSet.as_view({'get': 'list'})
        response = detail_view(request)
        response.render()
        trails = response.data['trails']
        self.assertEqual(len(trails), 2)

    def test_filtering_restroom(self):
        Trail.objects.create(
            name='Trilliam Lake',
            latitude=12.32,
            longitude=13.11,
            length=20.1,
            difficulty=4,
            restroom=False,
        )

        request = self.factory.get('/api/trails/', {'restroom': False})
        detail_view = TrailViewSet.as_view({'get': 'list'})
        response = detail_view(request)
        response.render()
        trails = response.data['trails']
        self.assertEqual(len(trails), 1)

    def test_filtering_length(self):
        Trail.objects.create(
            name='Trilliam Lake',
            latitude=12.32,
            longitude=13.11,
            length=1.1,
            difficulty=4,
            restroom=False,
        )

        request = self.factory.get('/api/trails/', {'length': 1.1})
        detail_view = TrailViewSet.as_view({'get': 'list'})
        response = detail_view(request)
        response.render()
        trails = response.data['trails']
        self.assertEqual(len(trails), 1)


    def test_filtering_length(self):
        Trail.objects.create(
            name='Trilliam Lake',
            latitude=12.32,
            longitude=13.11,
            length=1.1,
            difficulty=4,
            restroom=False,
        )

        request = self.factory.get('/api/trails/', {'length': 1.1, 'restroom': False})
        detail_view = TrailViewSet.as_view({'get': 'list'})
        response = detail_view(request)
        response.render()
        trails = response.data['trails']
        self.assertEqual(len(trails), 1)
