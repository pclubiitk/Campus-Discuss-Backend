from rest_framework import serializers
from .models import Stream
from posts.serializers import PostSerializer
from users.serializers import UserSerializer

class StreamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stream
        fields = (
            'title',
            'description',
            'pk',
        )

class PostByStreamSerializer(serializers.ModelSerializer):
    post_set = PostSerializer(many=True)
    class Meta:
        model = Stream
        fields = (
            'title',
            'post_set'
        )
        