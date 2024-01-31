from rest_framework import serializers

from blog.models import Blog


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ('title', 'author', 'image', 'created_at',)


class BlogSingleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ('title', 'author', 'image', 'content', 'views')


