from rest_framework import serializers
from .models import User
from posts.serializers import PostSerializer

class PostByAuthorSerializer(serializers.ModelSerializer):
    post_set=PostSerializer(many=True)
    class Meta:
        model=User
        fields=(
            'post_set',
            'username'
        )