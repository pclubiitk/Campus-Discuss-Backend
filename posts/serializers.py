from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):

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
        
