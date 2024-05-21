from rest_framework import serializers
from .models import Posting, Comment

class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    comments = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Posting
        fields = ['id', 'title', 'content', 'author', 'created_at', 'comments']

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Comment
        fields = ['id', 'post', 'content', 'author', 'created_at']
