"""models.py

Copyright © 2017 HikeOregon. All rights reserved.
Created by Bobby Eshleman on 2/18/2017.

"""


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
    restroom = models.BooleanField()

    def __str__(self):
        return self.name


class TrailImage(models.Model):
    trail = models.ForeignKey(Trail)
    image = models.ImageField(upload_to='trail_images/%Y/%m/%d/')
    timestamp = models.DateTimeField(auto_now_add=True)