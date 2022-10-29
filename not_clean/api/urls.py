from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import PostViewSet, expired_obtain_auth_token


router = SimpleRouter()
router.register(r'posts', PostViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('auth/', expired_obtain_auth_token)
]
