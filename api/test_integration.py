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

    def test_trail_list(self):
        url = reverse('trail-detail', kwargs={'pk': 1})
        response = self.client.get(url)
        response.render()
        self.assertEqual(response.data['name'], 'Multnomah Falls')
