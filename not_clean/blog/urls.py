from django.urls import path

from .views import PostListView, PostDetailView, AboutTemplateView, ContactCreateView


urlpatterns = [
    path('', PostListView.as_view(), name='main'),
    path('about/', AboutTemplateView.as_view(), name='about'),
    # path('api/posts/', PostApiView.as_view(), name='posts-api'),
    # path('api/posts/<int:post_id>/', PostApiView.as_view(), name='post-api'),
    path('contact/', ContactCreateView.as_view(), name='contact'),
    path('<slug:post_slug>/', PostDetailView.as_view(), name='post'),
]
