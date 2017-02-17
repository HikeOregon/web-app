from django.db import models

class Trail(models.Model):
    """Defines Trail data.  The data behind the trail list and trail detail
    API endpoint.

    ..note: Doesn't include weather, which should be on the front-end.

    Latitude and longitude support decimal places for precision up to one meter.

    """
    name = models.CharField(max_length=200)
    latitude = models.DecimalField(max_digits=7, decimal_places=5)
    longitude = models.DecimalField(max_digits=8, decimal_places=5)
    length = models.FloatField()
    difficulty = models.IntegerField()
    # Images should be a foreign key
    restroom = models.BooleanField()
