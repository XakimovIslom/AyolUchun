from django.contrib import admin
from course.models import Category, Tag, Course, CourseVideos, SocialApps, Interviews

# Register your models here.
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Course)
admin.site.register(CourseVideos)
admin.site.register(SocialApps)
admin.site.register(Interviews)
