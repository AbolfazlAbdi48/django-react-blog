from django.urls import path, include
from rest_framework import routers
from .views import (
    CategoryViewSet,
    ArticleViewSet,
    LikeView
)

router = routers.DefaultRouter()
router.register('categories', CategoryViewSet)
router.register('articles', ArticleViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('likes/', LikeView.as_view(), name='likes'),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]
