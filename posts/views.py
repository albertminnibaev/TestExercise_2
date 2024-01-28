from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from posts.models import Post, Comment
from posts.permissions import IsAdmin, IsAuthor
from posts.serializers import PostSerializer, CommentSerializer, PostCreateSerializer, CommentUpdateSerializer


class PostsViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()

    def get_permissions(self):
        if self.action in ['create']:
            return [IsAuthenticated()]
        if self.action in ['list']:
            return [((IsAuthor | IsAdmin) | (~IsAuthenticated))()]
        # if self.action in ['destroy', 'retrieve', 'update']:
        #     return [(IsAdmin | IsAuthor)()]
        return [(IsAuthor | IsAdmin)()]

    def perform_create(self, serializer):
        new_post = serializer.save()
        new_post.author = self.request.user
        new_post.save()

    def get_serializer_class(self):
        if self.action in ['create']:
            return PostCreateSerializer
        return PostSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()

    def get_permissions(self):
        if self.action in ['create']:
            return [IsAuthenticated()]
        if self.action in ['list']:
            return [((IsAuthor | IsAdmin) | (~IsAuthenticated))()]
        # if self.action in ['destroy', 'retrieve', 'update']:
        #     return [(IsAdmin | IsAuthor)()]
        return [(IsAuthor | IsAdmin)()]

    def perform_create(self, serializer):
        new_comments = serializer.save()
        new_comments.author = self.request.user
        new_comments.save()

    def get_serializer_class(self):
        if self.action in ['partial_update', 'update']:
            return CommentUpdateSerializer
        return CommentSerializer
