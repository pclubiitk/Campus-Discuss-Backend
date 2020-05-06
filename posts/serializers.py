from rest_framework import serializers
from .models import Post
from users.models import User
from users.serializers import UserSerializer

class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer()
    class Meta:
        model = Post
        fields = (
            "post_title",
            "post_text",
            "pub_date",
            "last_modified",
            "author",
            "stream"
        )

class PostByUserSerializer(serializers.ModelSerializer):
    post_set=PostSerializer(many=True)
    class Meta:
        model=User
        fields=(
            'post_set',
            'username'
        )
