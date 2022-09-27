from django.urls import path, include
from .views import ArticleViewSet, ArticleGenericViewSet, ArticleModelViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('article', ArticleViewSet, basename='article')
router.register('articlegenviewset', ArticleGenericViewSet, basename='articlegenviewset')
router.register('articlemodviewset', ArticleGenericViewSet, basename='articlegenviewset')



urlpatterns = [
    # link for viewsets
    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>', include(router.urls)),
    
    #  generic viewsets

    ]



