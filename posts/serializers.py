from datetime import datetime, timedelta, date

from rest_framework import serializers

from posts.models import Comment, Post
from posts.validators import TitleValidators


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ['author']


class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(source='comment_set', many=True, read_only=True)

    def validate_author(self, value):
        user = self.context['request'].user
        year_18 = user.date_of_birth.year + 18
        month = user.date_of_birth.month
        day = user.date_of_birth.day
        date_18 = date(year_18, month, day)
        if datetime.now().date() > date_18:
            return value
        raise serializers.ValidationError('автор поста не достиг возраста 18 лет')

    class Meta:
        model = Post
        fields = ['title', 'text', 'author', 'image', 'comments', 'created_at', 'date_of_change']
        validators = [
            TitleValidators(fields=('title',))
        ]
