from django.urls import reverse
from rest_framework.test import APIClient, APITestCase
from api.models import Trail

class TrailIntegrationTestCase(APITestCase):

    def setUp(self):
        Trail.objects.create(
            name='Multnomah Falls',
            latitude=12.32,
            longitude=13.11,
            length=20.1,
            difficulty=4,
            restroom=True,
        )

        Trail.objects.create(
            name='Trilliam Lake Loop',
            latitude=55.0,
            longitude=13.11,
            length=6.2,
            difficulty=3,
            restroom=False,
        )

    def test_trail_detail(self):
        url = reverse('trail-detail', kwargs={'pk': 1})
        response = self.client.get(url)
        response.render()
        self.assertEqual(response.data['name'], 'Multnomah Falls')

    def test_trail_list(self):
        url = reverse('trail-list')
        response = self.client.get(url)
        response.render()
        first_item = response.data[0]
        self.assertEqual(first_item['name'], 'Multnomah Falls')
        self.assertEqual(len(response.data), 2)

    def test_filter(self):
        url = reverse('trail-list')
        url += '?search=Lake'
        response = self.client.get(url, {'search': 'Lake'})
        response.render()
        self.assertEqual(len(response.data), 1)

        first_item = response.data[0]
        self.assertEqual(first_item['name'], 'Trilliam Lake Loop')
