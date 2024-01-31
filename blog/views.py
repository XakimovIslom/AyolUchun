from rest_framework.exceptions import ValidationError
from rest_framework.generics import ListAPIView, RetrieveAPIView

from blog.models import Blog
from blog.serializers import BlogSerializer, BlogSingleSerializer


class BlogListAPIView(ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class BlogSingleRetrieveAPIView(RetrieveAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSingleSerializer
