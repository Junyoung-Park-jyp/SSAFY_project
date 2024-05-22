from rest_framework import serializers
from .models import Post, Comment

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    total_likes = serializers.ReadOnlyField()

    class Meta:
        model = Comment
        fields = ['id', 'content', 'author', 'total_likes', 'created_at', 'likes']

class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    comments = CommentSerializer(many=True, read_only=True)
    total_likes = serializers.ReadOnlyField()
    comment_count = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'author', 'total_likes', 'created_at', 'comments', 'likes', 'comment_count']

    def get_comment_count(self, obj):
        return obj.comments.count()

