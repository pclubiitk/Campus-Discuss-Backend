from rest_framework import serializers
from .models import Stream
from posts.serializers import PostSerializer
from users.serializers import UserSerializer

class StreamSerializer(serializers.ModelSerializer):
    post_set = PostSerializer(many=True)
    followed_by = UserSerializer(many=True)
    class Meta:
        model = Stream
        fields = (
            'title',
            'description',
            'followed_by',
            'post_set'
        )

class PostByStreamSerializer(serializers.ModelSerializer):
    post_set = PostSerializer(many=True)
    class Meta:
        model = Stream
        fields = (
            'title',
            'post_set'
        )
        