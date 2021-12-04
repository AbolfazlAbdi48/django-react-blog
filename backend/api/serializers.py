from rest_framework import serializers
from blog.models import Article, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title', 'slug', 'is_active']
        lookup_field = 'slug'


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title','slug','description','image','is_active','categories','author']
        lookup_field = 'slug'
