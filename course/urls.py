from django.urls import path
from course.views import CategoryListAPIView, SocialAppsListAPIView, InterviewListAPIView, CourseListAPIView, \
    CourseAllListAPIView, AboutSingleCourseRetrieveAPIView

urlpatterns = [
    path('', CourseAllListAPIView.as_view()),
    path('course/<int:pk>/', AboutSingleCourseRetrieveAPIView.as_view()),
    path('course-by-category/', CourseListAPIView.as_view()),
    path('category/', CategoryListAPIView.as_view()),
    path('social-apps/', SocialAppsListAPIView.as_view()),
    path('interview/', InterviewListAPIView.as_view()),
]
