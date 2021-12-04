from django.urls import path, include
from rest_framework import routers
from .views import CategoryViewSet, ArticleViewSet

router = routers.DefaultRouter()
router.register('categories', CategoryViewSet)
router.register('articles', ArticleViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
