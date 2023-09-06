from rest_framework.routers import SimpleRouter

from .views import VoteViewSet

router = SimpleRouter()
router.register("",VoteViewSet,basename="vote")

urlpatterns = router.urls