from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import ContentViewSet

router = SimpleRouter()
router.register("",ContentViewSet,basename="content")

urlpatterns = router.urls