from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import PostViewSet


router = SimpleRouter()
router.register(r'posts', PostViewSet)


urlpatterns = [
    path('', include(router.urls))
]
