from django.db import models

from users.models import User


class Category(models.Model):
    title = models.CharField(max_length=211)
    image = models.ImageField(upload_to='category/')

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=221)

    def __str__(self):
        return self.title


class Course(models.Model):
    STATUS = (
        ('sotib_olingan', 'sotib_olingan'),
        ('sotib_olinmagan', 'sotib_olinmagan'),
    )

    title = models.CharField(max_length=221)
    image = models.ImageField(upload_to='course/')
    content = models.TextField()
    status = models.CharField(max_length=21, choices=STATUS, null=True, blank=True)

    # author =
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True, related_name='post')
    tag = models.ManyToManyField(Tag, related_name='tags')

    price = models.FloatField(max_length=100)
    discount = models.FloatField(max_length=221, blank=True, null=True)
    rating = models.FloatField(default=0)
    # is_bought = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class CourseVideos(models.Model):
    title = models.CharField(max_length=221)
    video = models.FileField(upload_to='course-videos/')

    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='videos')

    read_hour = models.IntegerField(null=True, blank=True)
    read_min = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.title


# class Video(models.Model):
#     lesson = models.ForeignKey(CourseVideos, on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)


class SocialApps(models.Model):
    instagram_url = models.CharField(max_length=221)
    tik_tok_url = models.CharField(max_length=221)
    you_tube_url = models.CharField(max_length=221)
    telegram_url = models.CharField(max_length=221)
    facebook_url = models.CharField(max_length=221)


class Interviews(models.Model):
    title = models.CharField(max_length=221)
    image = models.ImageField(upload_to='interviews/')
    # author
    read_hour = models.IntegerField()
    read_min = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.title
