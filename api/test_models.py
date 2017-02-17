from django.test import TestCase
from api.models import Trail

class TrailTestCase(TestCase):
    def setUp(self):
        Trail.objects.create(
            name='Multnomah Falls',
            latitude=12.32,
            longitude=13.11,
            length=20.1,
            difficulty=4,
            restroom=True,
        )

    def test_get(self):
        result = Trail.objects.get(name='Multnomah Falls')
        self.assertEqual(result.name, 'Multnomah Falls')
        self.assertEqual(result.latitude, 12.32)
        self.assertEqual(result.longitude, 13.11)
        self.assertEqual(result.length, 20.1)
        self.assertEqual(result.difficulty, 4)
        self.assertTrue(result.restroom)
