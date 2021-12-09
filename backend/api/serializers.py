from rest_framework import serializers
from drf_dynamic_fields import DynamicFieldsMixin
from blog.models import Article, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title', 'slug', 'is_active']
        lookup_field = 'slug'


class ArticleSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    def get_category(self, obj):
        return{
            "id": obj.categories.id,
            "title": obj.categories.title,
            "slug": obj.categories.slug
        }

    def get_author(self, obj):
        return{
            "id": obj.author.id,
            "username": obj.author.username,
            "full_name": obj.author.get_full_name(),
        }

    categories = serializers.SerializerMethodField("get_category")
    author = serializers.SerializerMethodField("get_author")

    class Meta:
        model = Article
        fields = ['id', 'title', 'slug', 'description',
                  'image', 'is_active', 'categories', 'author']
        lookup_field = 'slug'
