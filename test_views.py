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
        self.assertEqual(response.data['name'], 'Multnomah Falls')

    def test_list(self):
        request = self.factory.get('/api/trails/')
        detail_view = TrailViewSet.as_view({'get': 'list'})
        response = detail_view(request)
        response.render()
        first_item = response.data[0]
        self.assertEqual(first_item['name'], 'Multnomah Falls')
