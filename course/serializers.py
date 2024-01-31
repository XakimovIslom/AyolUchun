from rest_framework import serializers

from course.models import Category, Course, SocialApps, Interviews, CourseVideos


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('title',)


class CategorySerializer(serializers.ModelSerializer):
    post_count = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ('title', 'image', 'post_count')

    def get_post_count(self, obj):
        return obj.post.count()


class SocialAppSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialApps
        fields = ('instagram_url', 'tik_tok_url', 'you_tube_url', 'telegram_url', 'facebook_url')


class InterviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interviews
        fields = ('title', 'image', 'read_hour', 'read_min')


class CourseSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.title', read_only=True)
    tag_names = serializers.SerializerMethodField(required=False, read_only=True)

    class Meta:
        model = Course
        fields = (
            'title', 'image', 'category', 'tag_names', 'price',
            'rating')

    def get_tag_names(self, obj):
        tags = obj.tag.all()
        data = []
        for i in tags:
            data.append({'title': i.title})
        return data


class CourseAllSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.title', read_only=True)
    tag_names = serializers.SerializerMethodField(required=False, read_only=True)

    class Meta:
        model = Course
        fields = (
            'title', 'image', 'status', 'content', 'price', 'discount',
            'rating')


class AboutCourseSingleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('title', 'image', 'content', 'videos')
