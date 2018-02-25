from rest_framework import routers

from api.views import PostViewSet, VoteViewSet

router = routers.SimpleRouter()
router.register(r'posts', PostViewSet)
router.register(r'votes', VoteViewSet)
urlpatterns = router.urls
