"""test_urls.py

Copyright © 2017 HikeOregon. All rights reserved.
Created by Bobby Eshleman on 2/18/2017.

"""


from django.test import TestCase
from django.urls import reverse


class TrailURLTestCase(TestCase):

    def test_trail_detail_url(self):
        url = reverse('trail-detail', kwargs={'pk': 1})
        self.assertEqual(url, '/api/trails/1/')

    def test_trail_list_url(self):
        url = reverse('trail-list')
        self.assertEqual(url, '/api/trails/')
