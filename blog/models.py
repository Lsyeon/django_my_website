from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=30) #제목
    content = models.TextField() #내용

    created = models.DateTimeField() #작성일
    author = models.ForeignKey(User, on_delete=models.CASCADE) #어떤 사용자가 삭제되면 글도 삭제

    def __str__(self):
        return '{} :: {}'.format(self.title, self.author)