from rest_framework import serializers
from drf_dynamic_fields import DynamicFieldsMixin
from blog.models import Article, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title', 'slug', 'is_active']
        lookup_field = 'slug'


class ArticleSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
        lookup_field = 'slug'
