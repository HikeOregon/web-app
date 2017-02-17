from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Trail(models.Model):
    """Defines Trail data.  The data behind the trail list and trail detail
    API endpoint.

    ..note: Doesn't include weather, which should be on the front-end.

    """
    name = models.CharField(max_length=200)
    latitude = models.FloatField(validators=[MaxValueValidator(90.0), MinValueValidator(-90.0)])
    longitude = models.FloatField(validators=[MaxValueValidator(180.0), MinValueValidator(-180.0)])
    length = models.FloatField()
    difficulty = models.IntegerField()
    # Images should be a foreign key
    restroom = models.BooleanField()

    def __str__(self):
        string = 'Trail(name={}, latitude={}, longitude={}, length={}, '
        string += 'difficulty={}, restroom={})'

        return string.format(
                self.name,
                self.latitude,
                self.longitude,
                self.length,
                self.difficulty,
                self.restroom,
        )
