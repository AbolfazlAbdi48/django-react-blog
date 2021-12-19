from django.db import models
from django.contrib.auth import get_user_model
from .validators import validate_image

# Create your models here.

User = get_user_model()


class Category(models.Model):
    """
    The categories model,
    One-to-many relationship with articles.
    """
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    is_active = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return f'{self.title}'


class Article(models.Model):
    """
    The articles model.
    """
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='articles/images/', validators=[validate_image])
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



class Like(models.Model):
    """
    The main Like model,
    One-to-many relationship with User,
    One-to-many relationship with Article.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Like'
        verbose_name_plural = 'Likes'

    def __str__(self):
        return f'{self.owner} | {self.article}'