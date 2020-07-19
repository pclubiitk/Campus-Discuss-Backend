from rest_framework import serializers
from .models import Comment
from users.serializers import UserSerializer

class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Comment
        fields = (
            "pk",
            "parent",
            "post",
            "content",
            "created_at",
            "user",
        )
