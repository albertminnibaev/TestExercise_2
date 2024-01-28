from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from django.utils.http import urlencode

from posts.models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'text', 'image', 'created_at', 'date_of_change', 'view_author_link',
                    'view_comments_link')
    list_filter = ('created_at',)

    def view_comments_link(self, obj):
        count = obj.comment_set.count()
        url = (
            reverse("admin:posts_comment_changelist") + "?" + urlencode({"post__id": f"{obj.id}"})
        )
        return format_html('<a href="{}">{} Comments</a>', url, count)

    view_comments_link.short_description = "Comments"

    def view_author_link(self, obj):
        url = (
            reverse("admin:users_user_changelist") + "?" + urlencode({"id": f"{obj.author.id}"})
        )
        return format_html('<a href="{}">Author</a>', url)

    view_author_link.short_description = "Author"

    def get_model_perms(self, request):
        return {
            "add": self.has_add_permission(request),
            "change": self.has_change_permission(request),
            "delete": self.has_delete_permission(request),
            "view": self.has_view_permission(request),
        }

    def has_view_permission(self, request, obj=None):
        allowed = super().has_view_permission(request, obj)
        if object is None:
            return allowed
        return request.user.is_authenticated

    def has_change_permission(self, request, obj=None):
        allowed = super().has_change_permission(request, obj)
        if object is None:
            return allowed
        if obj is not None:
            return request.user.is_admin or request.user == obj.author
        return request.user.is_admin

    def has_add_permission(self, request):
        allowed = super().has_add_permission(request)
        if object is None:
            return allowed
        return request.user.is_authenticated

    def has_delete_permission(self, request, obj=None):
        allowed = super().has_delete_permission(request, obj)
        if object is None:
            return allowed
        if obj is not None:
            return request.user.is_admin or request.user == obj.author
        return request.user.is_admin


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'text', 'post', 'created_at', 'date_of_change')
    list_filter = ('post__id',)

    def get_model_perms(self, request):
        return {
            "add": self.has_add_permission(request),
            "change": self.has_change_permission(request),
            "delete": self.has_delete_permission(request),
            "view": self.has_view_permission(request),
        }

    def has_view_permission(self, request, obj=None):
        allowed = super().has_view_permission(request, obj)
        if object is None:
            return allowed
        return request.user.is_authenticated

    def has_change_permission(self, request, obj=None):
        allowed = super().has_change_permission(request, obj)
        if object is None:
            return allowed
        if obj is not None:
            return request.user.is_admin or request.user == obj.author
        return request.user.is_admin

    def has_add_permission(self, request):
        allowed = super().has_add_permission(request)
        if object is None:
            return allowed
        return request.user.is_authenticated

    def has_delete_permission(self, request, obj=None):
        allowed = super().has_delete_permission(request, obj)
        if object is None:
            return allowed
        if obj is not None:
            return request.user.is_admin or request.user == obj.author
        return request.user.is_admin
