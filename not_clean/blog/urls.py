from django.urls import path

from .views import PostListView, PostDetailView, AboutTemplateView, ContactCreateView


urlpatterns = [
    path('', PostListView.as_view(), name='main'),
    path('about', AboutTemplateView.as_view(), name='about'),
    path('contact', ContactCreateView.as_view(), name='contact'),
    path('<slug:post_slug>', PostDetailView.as_view(), name='post'),
]
