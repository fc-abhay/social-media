from rest_framework import serializers
from .models import Post, Comment, Like
from auths.serializer import UserSerializer

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = "__all__"

class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    likes = LikeSerializer(many=True, read_only=True)

    createdBy = UserSerializer(read_only=True)        # For GET response
    createdBy_id = serializers.UUIDField(write_only=True)  # For POST/PATCH

    class Meta:
        model = Post
        fields = "__all__"

