from django.db import models

from course.models import Category
from course.utils import BaseModel


class Blog(BaseModel):
    title = models.CharField(max_length=221)
    author = models.CharField(max_length=221)
    image = models.ImageField(upload_to='blog/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    content = models.TextField()
    views = models.IntegerField()

    def __str__(self):
        return self.title


