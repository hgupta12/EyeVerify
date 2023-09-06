from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import CommentViewSet

router = SimpleRouter()
router.register("",CommentViewSet,basename="comment")

urlpatterns = router.urls