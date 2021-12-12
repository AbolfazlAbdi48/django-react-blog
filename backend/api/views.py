from rest_framework import viewsets
from rest_framework.decorators import permission_classes
from blog.models import Article, Category
from .serializers import CategorySerializer, ArticleSerializer
from .permissions import (
    IsStaffOrReadOnly,
    IsAuthorOrReadOnly
)

# Create your views here.


class CategoryViewSet(viewsets.ModelViewSet):
    """
    The viewset for create, list, update and delete categories.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'


class ArticleViewSet(viewsets.ModelViewSet):
    """
    The viewset for create, list, update and delete articles.
    """
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    lookup_field = 'slug'
    filterset_fields = ['is_active', 'author']
    search_fields = ['title', 'description']

    def get_permissions(self):
        if self.action in ['list', 'create']:
            permission_classes = [IsStaffOrReadOnly]
        else:
            permission_classes = [IsStaffOrReadOnly, IsAuthorOrReadOnly]
        return [permission() for permission in permission_classes]
