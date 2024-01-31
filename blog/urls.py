from django.urls import path
from blog.views import BlogListAPIView, BlogSingleRetrieveAPIView

urlpatterns = [
    path('', BlogListAPIView.as_view()),
    path('blog/<int:pk>/', BlogSingleRetrieveAPIView.as_view()),
]

