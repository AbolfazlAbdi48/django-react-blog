from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from blog.models import Article, Category, Like
from .serializers import (
    CategorySerializer,
    ArticleSerializer,
    LikeSerializer
)
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


class LikeView(APIView):
    """
    List all likes or create a new like.
    """

    def get(self, request, foramt=None):
        likes = Like.objects.all()
        serializer = LikeSerializer(likes, many=True)
        return Response(serializer.data)

    def post(self, request, foramt=None):
        permission_classes = [IsAuthenticated]
        serializer = LikeSerializer(data=request.data)
        if serializer.is_valid():
            owner = request.user
            liked_article = serializer.validated_data['article']
            serializer.validated_data['owner'] = owner
            liked = Like.objects.filter(
                owner=owner, article=liked_article
            ).first()
            if liked:
                liked.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            else:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
