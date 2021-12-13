from rest_framework import serializers
from drf_dynamic_fields import DynamicFieldsMixin
from blog.models import Article, Category, Like


class CategorySerializer(serializers.ModelSerializer):
    """
    The main serializer for Category model.
    """
    class Meta:
        model = Category
        fields = ['id', 'title', 'slug', 'is_active']
        lookup_field = 'slug'


class ArticleSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    """
    The main serializer for Article model.
    """
    class Meta:
        model = Article
        fields = '__all__'
        lookup_field = 'slug'


class LikeSerializer(serializers.ModelSerializer):
    """
    The main serializer for Like model.
    """
    class Meta:
        model = Like
        fields = '__all__'
