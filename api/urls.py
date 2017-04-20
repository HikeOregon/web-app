"""urls.py

Copyright © 2017 HikeOregon. All rights reserved.
Created by Bobby Eshleman on 2/18/2017.

"""


from rest_framework import routers
from api.views import TrailViewSet, TrailImageViewSet


router = routers.DefaultRouter()
router.register(r'trails', TrailViewSet)
router.register(r'trail_images', TrailImageViewSet)
urlpatterns = router.urls
