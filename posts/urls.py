from django.urls import path, include
from rest_framework.routers import DefaultRouter

from posts.apps import PostsConfig
from posts.views import PostsViewSet, CommentViewSet

app_name = PostsConfig.name

posts_router = DefaultRouter()
posts_router.register(r'posts', PostsViewSet, basename='posts')
comments_router = DefaultRouter()
comments_router.register(r'comments', CommentViewSet, basename='comments')

urlpatterns = [
    path('', include(posts_router.urls)),
    path('', include(comments_router.urls)),
]
