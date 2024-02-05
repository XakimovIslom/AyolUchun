from django.urls import path
from blog.views import BlogListAPIView

urlpatterns = [
    path("", BlogListAPIView.as_view()),
]
