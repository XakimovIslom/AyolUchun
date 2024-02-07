from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView, RetrieveAPIView

from course.models import Category, Course, Interviews, SocialApps
from course.serializers import (
    AboutCourseSingleSerializer,
    CategorySerializer,
    CourseAllSerializer,
    CourseSerializer,
    InterviewSerializer,
    SocialAppSerializer,
)


class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.all().order_by("?")[:8]
    serializer_class = CategorySerializer


class SocialAppsListAPIView(ListAPIView):
    queryset = SocialApps.objects.all()
    serializer_class = SocialAppSerializer


class InterviewListAPIView(ListAPIView):
    queryset = Interviews.objects.all()
    serializer_class = InterviewSerializer


class CourseListAPIView(ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ("category",)

    # def get_queryset(self):
    #     queryset = Course.objects.all()
    #     category = self.request.query_params.get('category')
    #     if category:
    #         queryset = queryset.filter(category__title=category)
    #     return queryset


class CourseAllListAPIView(ListAPIView):
    queryset = Course.objects.all().order_by("id")[:4]
    serializer_class = CourseAllSerializer


class AboutSingleCourseRetrieveAPIView(RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = AboutCourseSingleSerializer
