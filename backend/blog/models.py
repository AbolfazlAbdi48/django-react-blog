from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()


class Category(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField()
    is_active = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return f'{self.title}'


class Article(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='articles/images/')
    is_active = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    def __str__(self):
        return f'{self.title}'
