from django.test import TestCase
from django.core.exceptions import ValidationError

from api.models import Trail

class TrailTestCase(TestCase):

    field_kwargs = dict(
            name='Multnomah Falls',
            latitude=12.32,
            longitude=13.11,
            length=20.1,
            difficulty=4,
            restroom=True,
    )

    def setUp(self):
        Trail.objects.create(**self.field_kwargs)

    def test_get(self):
        result = Trail.objects.get(name='Multnomah Falls')
        self.assertEqual(result.name, 'Multnomah Falls')
        self.assertEqual(result.latitude, 12.32)
        self.assertEqual(result.longitude, 13.11)
        self.assertEqual(result.length, 20.1)
        self.assertEqual(result.difficulty, 4)
        self.assertTrue(result.restroom)
