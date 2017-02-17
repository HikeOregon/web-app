from rest_framework import routers
from api.views import TrailViewSet

router = routers.DefaultRouter()
router.register(r'trails', TrailViewSet)
urlpatterns = router.urls
