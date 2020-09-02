from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=30) #제목
    content = models.TextField() #내용

    head_image = models.ImageField(upload_to='blog/%Y/%m/%d/', blank=True) # 이미지 시간별로 구분, 필수로 안채워져도 됨

    created = models.DateTimeField() #작성일
    author = models.ForeignKey(User, on_delete=models.CASCADE) #어떤 사용자가 삭제되면 글도 삭제

    def __str__(self):
        return '{} :: {}'.format(self.title, self.author)

    def get_absolute_url(self):
        return '/blog/{}/'.format(self.pk) #admin에서 사이트이동

