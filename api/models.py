from django.db import models

class Trail(models.Model):
    """Defines Trail data.  The data behind the trail list and trail detail
    API endpoint.

    ..note: Doesn't include weather, which should be on the front-end.

    """
    name = models.CharField(max_length=200)
    latitude = models.FloatField()
    longitude = models.FloatField()
    length = models.FloatField()
    difficulty = models.IntegerField()
    # Images should be a foreign key
    restroom = models.BooleanField()
