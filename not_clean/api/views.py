from rest_framework.viewsets import ModelViewSet

from .serializers import PostSerializer
from blog.models import Post


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all().order_by('date_published')
    serializer_class = PostSerializer
