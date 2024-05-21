from rest_framework import serializers
from .models import Posting, Comment

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Comment
        fields = ['id', 'post', 'content', 'author', 'created_at', 'updated_at', 'total_likes']

class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    comments = CommentSerializer(many=True, read_only=True)
    total_likes = serializers.IntegerField(source='total_likes', read_only=True)

    class Meta:
        model = Posting
        fields = ['id', 'title', 'content', 'author', 'created_at', 'updated_at', 'total_likes', 'comments']
