from django.db import models
from utils.models import BaseModel
from users.models import User


class Course(BaseModel):
    title = models.CharField(max_length=211)
    image = models.ImageField(upload_to="course/")
    description = models.TextField(blank=True)
    buy_user = models.ManyToManyField(User, related_name="buy_course", blank=True)

    price = models.IntegerField(default=0)
    price_discount = models.IntegerField(default=0, null=True)

    def __str__(self):
        return self.title


class Lesson(BaseModel):
    title = models.CharField(max_length=211)
    total_time = models.IntegerField(default=0)  # seconds, Example: 5 min = 300 sec

    def __str__(self):
        return self.title


class LessonUser(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    time_watched = models.IntegerField(default=0)  # 280  # seconds, Example: 5 min = 300 sec
    total_time = models.IntegerField(default=0)  # 300  # seconds, Example: 5 min = 300 sec

    def __str__(self):
        return f"{self.user} - {self.lesson}"

    def is_finished(self):
        return self.total_time * 0.9 <= self.time_watched

    @property
    def status(self):
        if self.is_finished():
            return "finished"
        if self.time_watched > 0:
            return "in_progress"
        return "not started"


class LessonUserWatched(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(LessonUser, on_delete=models.CASCADE)

    from_time = models.IntegerField(default=0)
    to_time = models.IntegerField(default=0)
