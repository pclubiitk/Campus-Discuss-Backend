from rest_framework import serializers
from .models import Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            "pk",
            "parent",
            "post",
            "content",
            "created_at",
            "user"
        )
