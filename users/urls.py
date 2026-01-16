from rest_framework.routers import DefaultRouter
from .views import UserProfileViewSet

router = DefaultRouter()
router.register(r'users', UserProfileViewSet, basename='userprofile')
urlpatterns = router.urls