from rest_framework import serializers

from blog.models import Post
from slugify import slugify


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        exclude = ('slug', )

    def create(self, validated_data):
        post = Post(
            **validated_data | {
                'slug': slugify(validated_data.get('title') + '-' + validated_data.get('subtitle'))
            }
        )
        post.save()
        return post
