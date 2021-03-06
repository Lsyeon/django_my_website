from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=25, unique=True)
    description = models.TextField(blank=True)

    slug = models.SlugField(unique=True, allow_unicode=True) #유니코드를 허용

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return '/blog/category/{}/'.format(self.slug)

    class Meta:
        verbose_name_plural = 'categories'

class Tag(models.Model):
    name = models.CharField(max_length=40, unique=True)
    slug = models.SlugField(unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return '/blog/tag/{}/'.format(self.slug)


class Post(models.Model):
    title = models.CharField(max_length=30) #제목
    content = models.TextField() #내용

    head_image = models.ImageField(upload_to='blog/%Y/%m/%d/', blank=True) # 이미지 시간별로 구분, 필수로 안채워져도 됨

    created = models.DateTimeField(auto_now_add=True) #작성일
    author = models.ForeignKey(User, on_delete=models.CASCADE) #어떤 사용자가 삭제되면 글도 삭제

    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.SET_NULL)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return '{} :: {}'.format(self.title, self.author)

    def get_absolute_url(self):
        return '/blog/{}/'.format(self.pk) #admin에서 사이트이동

    def get_update_url(self):
        return self.get_absolute_url() + 'update'
