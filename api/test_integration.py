"""test_integration.py

Copyright © 2017 HikeOregon. All rights reserved.
Created by Bobby Eshleman on 2/18/2017.

"""


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
        first_trail = response.data['trails'][0]
        self.assertEqual(first_trail['name'], 'Multnomah Falls')

    def test_trail_list(self):
        url = reverse('trail-list')
        response = self.client.get(url)
        response.render()
        trails = response.data['trails']
        self.assertEqual(len(trails), 2)
        self.assertEqual(trails[0]['name'], 'Multnomah Falls')

    def test_filter(self):
        url = reverse('trail-list')
        url += '?search=Lake'
        response = self.client.get(url, {'search': 'Lake'})
        response.render()
        self.assertEqual(len(response.data), 1)

        first_trail = response.data['trails'][0]
        self.assertEqual(first_trail['name'], 'Trilliam Lake Loop')
