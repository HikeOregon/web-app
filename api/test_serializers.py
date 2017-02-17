from django.test import TestCase
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
        serializer = TrailSerializer(trail)
        fields = self.fields.copy()
        fields['id'] = 1
        self.assertDictEqual(serializer.data, fields)
